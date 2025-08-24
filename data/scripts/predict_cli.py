#!/usr/bin/env python3
"""
Prediction CLI for CNOC baseline model
Takes free-text input and outputs top-3 NCO predictions with confidences
"""

import joblib
import numpy as np
from pathlib import Path

MODELS = Path("models")

# load model + vectorizer
clf = joblib.load(MODELS / "tfidf_logreg.pkl")
vectorizer = joblib.load(MODELS / "tfidf_vectorizer.pkl")

# optional: map 2-digit NCO to names
NCO_MAJOR_GROUPS = {
    "11": "Legislators & Senior Officials",
    "21": "Science & Engineering Professionals",
    "22": "Health Professionals",
    "23": "Teaching Professionals",
    "24": "Business & Administration Professionals",
    "31": "Science & Engineering Associate Professionals",
    "32": "Health Associate Professionals",
    "33": "Business & Administration Associate Professionals",
    "34": "Legal, Social, Cultural Professionals",
    "35": "Information & Communications Technicians",
    "41": "General & Keyboard Clerks",
    "42": "Customer Services Clerks",
    "43": "Numerical & Material Recording Clerks",
    "44": "Other Clerical Support Workers",
    "51": "Personal Service Workers",
    "52": "Sales Workers",
    "53": "Personal Care Workers",
    "54": "Protective Services Workers",
    "61": "Market-Oriented Skilled Agricultural Workers",
    "62": "Subsistence Farmers, Fishers, Hunters",
    "63": "Forestry, Fishery, Hunting Workers",
    "71": "Building & Related Trades Workers",
    "72": "Metal, Machinery & Related Trades Workers",
    "73": "Handicraft & Printing Trades Workers",
    "74": "Electrical & Electronic Trades Workers",
    "75": "Food Processing, Woodworking, Garment Trades",
    "81": "Stationary Plant & Machine Operators",
    "82": "Assembly Workers",
    "83": "Drivers & Mobile Plant Operators",
    "91": "Cleaners & Helpers",
    "92": "Agricultural, Forestry, Fishery Labourers",
    "93": "Labourers in Mining, Construction, Transport",
    "94": "Food Preparation Assistants",
    "95": "Street & Related Sales/Service Workers",
    "96": "Refuse Workers & Other Elementary Labourers",
}

def predict(text, top_k=3):
    X = vectorizer.transform([text])
    probs = clf.predict_proba(X)[0]
    classes = clf.classes_

    top_idx = np.argsort(probs)[::-1][:top_k]
    results = []
    for idx in top_idx:
        code = classes[idx]
        label = NCO_MAJOR_GROUPS.get(code, "Unknown")
        results.append((code, label, probs[idx]))
    return results

def main():
    print("\n🔮 CNOC Occupation Classifier (TF-IDF baseline)")
    print("Type a job description (English). Type 'exit' to quit.\n")

    while True:
        text = input("Enter description: ").strip()
        if text.lower() in ["exit", "quit"]:
            break
        preds = predict(text)
        print("🔎 Predictions:")
        for code, label, prob in preds:
            print(f"  {code} ({label}) → {prob*100:.2f}%")
        print()

if __name__ == "__main__":
    main()
