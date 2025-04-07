import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load cleaned logs
log_file = "logs/cleaned_logs.txt"

try:
    with open(log_file, "r", encoding="utf-8") as f:
        logs = [line.strip() for line in f.readlines() if line.strip()]  # Remove empty lines

    if not logs:
        raise ValueError("❌ Log file is empty! Check preprocess_logs.py.")

except FileNotFoundError:
    raise FileNotFoundError(f"❌ Log file not found: {log_file}")

# Identify failures
labels = ["Failure" if "error" in log.lower() or "failed" in log.lower() else "Success" for log in logs]

# Debug: Count failures & successes
num_failures = labels.count("Failure")
num_successes = labels.count("Success")
print(f"🔹 Found {num_failures} failure logs and {num_successes} success logs.")

if num_failures == 0:
    raise ValueError("❌ No failure logs found! AI model needs failure data to learn.")

# Create DataFrame
df = pd.DataFrame({"log": logs, "label": labels})

# Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["log"])

# Check if vectorization is empty
if X.shape[1] == 0:
    raise ValueError("❌ TF-IDF transformation failed: No useful words found!")

y = np.array([1 if label == "Failure" else 0 for label in df["label"]])

# Train-test split (safe version)
if len(y) < 2:
    print("⚠️ Not enough data to split — training on full dataset.")
    X_train, y_train = X, y
    X_test, y_test = X, y
else:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model & vectorizer
joblib.dump(model, "models/failure_predictor.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model trained and saved!")
