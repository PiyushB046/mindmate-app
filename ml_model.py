# ml_model.py

import joblib

# Load the model and vectorizer
model = joblib.load("models/mental_health_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_label(user_input):
    """Predict mental health label based on user input text."""
    text_vector = vectorizer.transform([user_input])
    prediction = model.predict(text_vector)
    return prediction[0]
