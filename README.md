
---

# CrossLingual Neural Occupation Classifier (CNOC)

AI-powered **Multilingual Occupational Classification Assistant** that maps natural language job descriptions to **NCO-2015 occupation codes** **[** [codes-file1](/docs/National_Classification_of_Occupations_Vol_I-2015.pdf) **,** [codes-file2a](/docs/National_Classification_of_Occupations_Vol_II-A-2015.pdf) **,** [codes-file2b](/docs/National_Classification_of_Occupations_Vol_II-B-2015.pdf) **]** for government surveys and workforce analytics.

-------------

## 🚀 Features

* 🌐 **Multilingual Support**: Handles job descriptions in English, Tamil, Hindi (extensible to other Indian languages).
* 🤖 **Hybrid Semantic Engine**: Uses **MuRIL/IndicBERT embeddings** + **FAISS + BM25** hybrid search for accurate classification.
* 🎙️ **Voice-to-Code Pipeline**: Supports speech-based inputs via **SpeechRecognition + gTTS**.
* 📊 **Active Learning Loop**: Confidence scoring with human feedback for continuous improvement.
* 🔒 **Secure & Deployable**: On-prem deployment with encryption and audit logs for government readiness.
* 📑 **Cultural Context Embeddings**: Handles regional terminology and linguistic variations.

-------------
## 📏Project Architecture:

-------------

## 🛠 Tech Stack

* **Languages**: Python
* **Models**: MuRIL, IndicBERT, Hugging Face Transformers,XLM-RoBERTa
* **Search & IR**: FAISS, BM25
* **Libraries/Frameworks**: PyTorch, Streamlit
* **Speech & Multilingual Tools**: SpeechRecognition, gTTS
* **Other**: Docker (optional deployment)

-------------

## 📂 Project Structure

```
CrossLingual-Neural-Occupation-Classifier-CNOC/
│
├── cnoc-data/                         # 🔹 Data engineering pipeline
│   ├── raw/                           # Raw scraped files
│   │   ├── nat_page_000.csv
│   │   ├── nat_page_001.csv
│   │   └── nat_all.csv / nat_all.json
│   │
│   ├── interim/                       # Cleaned & normalized
│   │   └── nat_clean.csv / nat_clean.parquet
│   │
│   ├── processed/                     # Ready-to-train datasets
│   │   └── train_rows.csv / train_rows.parquet
│   │
│   ├── scripts/                       # Python scripts
│   │   ├── scrape_nat.py              # Step 1: Scraping
│   │   ├── clean_nat.py               # Step 2: Cleaning
│   │   ├── augment_multilingual.py    # Step 3: Multilingual Expansion
│   │   └── (future: embed_index.py, train_model.py, etc.)
│   │
│   ├── notebooks/                     # Jupyter experiments
│   │   └── EDA.ipynb
│   │
│   ├── logs/                          # Run logs (scraping, training)
│   └── README.md                      # Mini-guide for data pipeline
│
├── cnoc-model/                        # 🔹 Model training & evaluation
│   ├── configs/                       # Model configs (json/yaml)
│   ├── checkpoints/                   # Saved models
│   ├── scripts/                       # Training/inference scripts
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── infer.py
│   └── notebooks/                     # Model prototyping
│
├── cnoc-api/                          # 🔹 Serving layer
│   ├── app.py                         # FastAPI / Flask service
│   ├── requirements.txt
│   └── Dockerfile
│
├── docs/                              # 🔹 Documentation
│   ├── CNOC_NAT_Data_Pipeline_Guide.pdf
│   ├── proposal.pdf
│   └── diagrams/                      # (optional) pipeline charts
│
├── tests/                             # 🔹 Unit tests
│
├── requirements.txt                   # Common dependencies
├── pyproject.toml / setup.py          # (if packaging as a module)
└── README.md                          # High-level project overview

```

-------------

## ⚡ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/ashwin-r11/CrossLingual-Neural-Occupation-Classifier-CNOC.git
cd CrossLingual-Neural-Occupation-Classifier-CNOC
pip install -r requirements.txt
```

-------------

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run src/app.py
```

Example input:

```
"Patient care assistant in rural hospital"
```

Output:

```
NCO-2015 Code: 3258 - Health Care Assistant
Confidence: 87%
```

-------------

## 📊 Demo

(Add screenshots / GIFs of your Streamlit UI here once available)

-------------

## 📜 Proposal
### Access the full proposal

Use either link below. If one fails or is restricted, try the alternate mirror. Both point to the same PDF.

**Brief overview:**
- **Objectives:** Multilingual NCO-2015 classification for surveys and analytics.
- **Method:** MuRIL/IndicBERT embeddings with FAISS + BM25 hybrid retrieval; active learning   
  with human-in-the-loop.
- **Deliverables:** cleaned datasets, training scripts/checkpoints, search index, REST API,  
  Streamlit UI, and documentation.
- **Governance:** data sourcing, privacy, and audit logging for on-prem deployments.
- **Timeline:** phased milestones with accuracy/coverage targets and evaluation protocols.
- **Risks & mitigations:** domain drift, OOV terms, low-resource variance; fallback IR and continuous feedback.

📄 **[** [Read Full Proposal link-1](https://drive.google.com/file/d/1rsMgQqcf3KDEjrUDRJUxFrlFDeTencet/view?usp=sharing) **]<----CLICK HERE**

📄 **[** [Read Full Proposal link-2](/docs/VrittiDisha_AI(LongTerm).pdf) **]<----CLICK HERE**

-------------

## 🤝 Contribution
Contributions are welcome. Please read the CONTRIBUTING.md guide before opening an issue or submitting a pull request.


Read the full guide: CONTRIBUTING.md

-------------


# 📧 Contact
##### *-----------------------anyone below---------*
**Ashwin R**
📩 [mail.to.ashwinr.tn@gmail.com](mailto:mail.to.ashwinr.tn@gmail.com) | [LinkedIn](https://www.linkedin.com/in/ashwin-r11/) | [GitHub](https://github.com/Ashwin-r11)

**Aniruddh SB**
📩 [aniruddhsb2005@gmail.com](mailto:aniruddhsb2005@gmail.com) | [LinkedIn](http://www.linkedin.com/in/aniruddh-sb-b64b32288) | [GitHub](https://github.com/Aniruddh-ui)

**ManiKandan S**
📩 [maniofficial.ac.in@gmail.com](maniofficial.ac.in@gmail.com) | [LinkedIn](https://www.linkedin.com/in/manikandan-s-166781301) | [GitHub](https://github.com/mani30mk)

**Balaji BP**
📩 [127158006@sastra.ac.in](mailto:127158006@sastra.ac.in) | [LinkedIn](https://www.linkedin.com/in/balaji-b-p-243853300) | [GitHub]()


-------------

## 📄 License

This project is licensed under the Apache License 2.0.

- Copyright (c) 2025 CNOC Contributors
- License file: [LICENSE](/LICENSE)

```
==========================IMPORTANT NOTE===========================================
      Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an "AS IS" BASIS,
without warranties or conditions of any kind. See the LICENSE file for details.

```

---
