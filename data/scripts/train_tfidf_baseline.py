#!/usr/bin/env python3
"""
Baseline: TF-IDF + Logistic Regression for NCO Code Classification (Major Group level)
- Trains on English text
- Saves model + vectorizer
- Supports interactive CLI predictions with confidence scores
"""

import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
import numpy as np

PROCESSED = Path("processed")
MODELS = Path("models")
MODELS.mkdir(exist_ok=True)

POSSIBLE_TEXT_COLUMNS = ["english_text", "occupation_title", "text", "hi_text", "ta_text"]

def detect_text_column(df):
    for col in POSSIBLE_TEXT_COLUMNS:
        if col in df.columns:
            return col
    raise ValueError(f"No known text column found in {df.columns}")

def load_data():
    train = pd.read_csv(PROCESSED / "train.csv")
    val   = pd.read_csv(PROCESSED / "val.csv")
    test  = pd.read_csv(PROCESSED / "test.csv")
    return train, val, test

def train_model():
    train, val, test = load_data()
    print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")

    text_col = detect_text_column(train)
    print(f"✅ Using text column: {text_col}")

    # Collapse to 2-digit NCO major group
    for df in [train, val, test]:
        df["nco_major"] = df["nco_2015"].astype(str).str[:2]

    X_train, y_train = train[text_col].astype(str), train["nco_major"]
    X_val,   y_val   = val[text_col].astype(str), val["nco_major"]
    X_test,  y_test  = test[text_col].astype(str), test["nco_major"]

    # TF-IDF vectorizer
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_val_tfidf   = vectorizer.transform(X_val)
    X_test_tfidf  = vectorizer.transform(X_test)

    # Logistic Regression classifier
    clf = LogisticRegression(max_iter=300, solver="saga", n_jobs=-1)
    clf.fit(X_train_tfidf, y_train)

    # Validation
    val_preds = clf.predict(X_val_tfidf)
    print("\nValidation Report:")
    print(classification_report(y_val, val_preds, zero_division=0))

    # Test
    test_preds = clf.predict(X_test_tfidf)
    print("\nTest Report:")
    print(classification_report(y_test, test_preds, zero_division=0))
    print("Test Accuracy:", accuracy_score(y_test, test_preds))

    # Save model + vectorizer
    joblib.dump(clf, MODELS / "tfidf_logreg.pkl")
    joblib.dump(vectorizer, MODELS / "tfidf_vectorizer.pkl")
    print("✅ Saved model and vectorizer in models/")

def interactive_cli():
    clf = joblib.load(MODELS / "tfidf_logreg.pkl")
    vectorizer = joblib.load(MODELS / "tfidf_vectorizer.pkl")

    print("\n🔮 CNOC Occupation Classifier (TF-IDF baseline)")
    print("Type a job title (English). Type 'exit' to quit.\n")

    while True:
        text = input("Enter occupation: ").strip()
        if text.lower() in ["exit", "quit"]:
            break
        X = vectorizer.transform([text])
        probs = clf.predict_proba(X)[0]
        classes = clf.classes_

        # Top 3 predictions
        top_idx = np.argsort(probs)[::-1][:3]
        print("🔎 Predictions:")
        for idx in top_idx:
            print(f"  {classes[idx]} → {probs[idx]*100:.2f}%")
        print()

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--predict", action="store_true", help="Run interactive CLI for predictions")
    args = parser.parse_args()

    if args.predict:
        interactive_cli()
    else:
        train_model()

if __name__ == "__main__":
    main()
