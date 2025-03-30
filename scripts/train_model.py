import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load cleaned logs
log_file = "logs/cleaned_logs.txt"

with open(log_file, "r", encoding="utf-8") as f:
    logs = f.readlines()

# Create labels: "Failure" if log contains "error" or "failed", else "Success"
labels = ["Failure" if "error" in log.lower() or "failed" in log.lower() else "Success" for log in logs]

# Convert logs into a DataFrame
df = pd.DataFrame({"log": logs, "label": labels})

# Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["log"])
y = np.array([1 if label == "Failure" else 0 for label in df["label"]])  # 1 = Failure, 0 = Success

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(model, "models/failure_predictor.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model trained and saved!")
