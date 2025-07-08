# train_model.py

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os

# Load real dataset
df = pd.read_csv("Mental-Health-Classification-Dataset/data/combined_data.csv")

# Keep only relevant labels
labels = ["Normal", "Anxiety", "Depression", "Stress"]
df = df[df["status"].isin(labels)]
df = df[["statement", "status"]].dropna()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["statement"], df["status"], test_size=0.2, random_state=42, stratify=df["status"]
)

# Vectorize text
vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model + vectorizer
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/mental_health_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
print("✅ Trained model and vectorizer saved in /models")
