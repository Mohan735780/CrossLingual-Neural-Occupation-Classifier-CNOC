
---

# CrossLingual Neural Occupation Classifier (CNOC)

AI-powered **Multilingual Occupational Classification Assistant** that maps natural language job descriptions to **NCO-2015 occupation codes** for government surveys and workforce analytics.

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
* **Models**: MuRIL, IndicBERT, Hugging Face Transformers
* **Search & IR**: FAISS, BM25
* **Libraries/Frameworks**: PyTorch, Streamlit
* **Speech & Multilingual Tools**: SpeechRecognition, gTTS
* **Other**: Docker (optional deployment)

-------------

## 📂 Project Structure


```text
CNOC/
├── src/                              # Application source
│   ├── app.py                        # Streamlit entrypoint
│   ├── __init__.py
│   ├── config/                       # App/config management
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── preprocessing/                # Text cleaning & tokenization
│   │   ├── __init__.py
│   │   ├── clean.py
│   │   └── tokenize.py
│   ├── semantic/                     # Embeddings + FAISS
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   └── faiss_index.py
│   ├── hybrid/                       # FAISS + BM25 fusion
│   │   ├── __init__.py
│   │   └── rerank_bm25.py
│   ├── speech/                       # Speech I/O pipeline
│   │   ├── __init__.py
│   │   ├── stt.py
│   │   └── tts.py
│   ├── evaluation/                   # Metrics & reports
│   │   ├── __init__.py
│   │   └── metrics.py
│   └── utils/                        # Shared helpers
│       ├── __init__.py
│       ├── io.py
│       └── logging.py
├── data/
│   ├── raw/                          # Raw datasets (job descriptions)
│   ├── processed/                    # Cleaned/augmented datasets
│   └── external/                     # NCO-2015 mappings/dictionaries
├── models/
│   ├── checkpoints/                  # Fine-tuned weights
│   └── indexes/                      # FAISS indexes
├── resources/
│   └── nco_2015/                     # Taxonomy CSV/JSON, codebook
├── scripts/                          # CLI utilities
│   ├── prepare_data.py
│   ├── build_index.py
│   └── evaluate.py
├── notebooks/                        # Experiments & EDA (optional)
├── tests/                            # Unit/integration tests
│   └── test_app.py
├── assets/                           # Images/GIFs for README/demo
├── .env.example                      # Sample environment variables
├── requirements.txt
├── pyproject.toml                    # Tooling/formatters (optional)
├── Dockerfile                        # Containerization (optional)
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
└── LICENSE

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

📄 **[** [Read Full Proposal](https://drive.google.com/file/d/1rsMgQqcf3KDEjrUDRJUxFrlFDeTencet/view?usp=sharing) **]<----CLICK HERE**

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
