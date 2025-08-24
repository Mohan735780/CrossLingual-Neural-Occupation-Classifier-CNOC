#!/usr/bin/env python3
"""
Augment NCO dataset with multilingual variants (English, Hindi, Tamil).

Input : interim/nat_clean.parquet
Output: processed/train_rows.parquet + processed/train_rows.csv
"""

import pandas as pd
from pathlib import Path
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from IndicTransToolkit.processor import IndicProcessor

# Paths
INTERIM = Path("interim")
PROCESSED = Path("processed"); PROCESSED.mkdir(exist_ok=True)

# Device setup
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🔄 Using device: {DEVICE}")

# Load model + tokenizer (use distilled 200M version to avoid OOM)
print("🔄 Loading IndicTrans2 distilled model...")
MODEL_NAME = "ai4bharat/indictrans2-en-indic-dist-200M"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32
).to(DEVICE)

ip = IndicProcessor(inference=True)

def translate_to_language(texts, src_lang, tgt_lang, batch_size=32):
    """Translate a list of texts in small batches to avoid OOM + cache bug"""
    translations = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        batch = ip.preprocess_batch(batch_texts, src_lang=src_lang, tgt_lang=tgt_lang)
        inputs = tokenizer(
            batch, truncation=True, padding="longest", return_tensors="pt"
        ).to(DEVICE)

        with torch.no_grad():
            tokens = model.generate(
                **inputs,
                max_length=128,
                num_beams=1,        # greedy decoding only
                do_sample=False,    # disable sampling
                use_cache=False     # 🚑 critical fix for cache KeyError
            )

        dec = tokenizer.batch_decode(tokens, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        translations.extend(ip.postprocess_batch(dec, lang=tgt_lang))
        print(f"   ✅ Batch {i//batch_size + 1}/{len(texts)//batch_size + 1} done")

    return translations

def make_training_rows(df):
    rows = []
    texts = df["title"].tolist()
    ncos = df["nco_2015"].tolist()

    print("🔄 Translating to Hindi...")
    hi_translations = translate_to_language(texts, "eng_Latn", "hin_Deva")

    print("🔄 Translating to Tamil...")
    ta_translations = translate_to_language(texts, "eng_Latn", "tam_Taml")

    for eng, nco, hi, ta in zip(texts, ncos, hi_translations, ta_translations):
        rows.append({"lang": "en", "text": eng, "nco_2015": nco})
        if hi and hi != eng:
            rows.append({"lang": "hi", "text": hi, "nco_2015": nco})
        if ta and ta != eng:
            rows.append({"lang": "ta", "text": ta, "nco_2015": nco})

    return pd.DataFrame(rows)

def main():
    df = pd.read_parquet(INTERIM / "nat_clean.parquet")
    print(f"✅ Loaded {len(df)} rows from interim/nat_clean.parquet")

    out = make_training_rows(df)
    print(f"✅ Generated {len(out)} multilingual rows "
          f"({out['lang'].value_counts().to_dict()})")

    out.to_parquet(PROCESSED / "train_rows.parquet", index=False)
    out.to_csv(PROCESSED / "train_rows.csv", index=False)
    print("✅ Saved multilingual dataset in processed/")

if __name__ == "__main__":
    main()
