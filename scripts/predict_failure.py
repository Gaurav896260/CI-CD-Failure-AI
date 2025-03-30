import joblib

# Load the trained model and vectorizer
model = joblib.load("models/failure_predictor.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_failure(log_message):
    """Predict if the log message will cause a failure."""
    log_features = vectorizer.transform([log_message])  # Convert text to features
    prediction = model.predict(log_features)
    
    return "Failure Expected" if prediction[0] == 1 else "No Failure"

# Example usage
log_input = "Error: Database connection failed due to timeout"
result = predict_failure(log_input)
print(f"🔹 Prediction: {result}")
