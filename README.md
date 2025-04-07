# CI/CD Failure AI

## Goal:

Utilize AI/ML to analyze past CI/CD logs and predict build failures before they occur.

## ✨ Features:

- Predict build failures using machine learning.
- Integrate the AI model into CI/CD pipelines (GitHub Actions included).
- Preprocess and clean logs automatically.
- Store and reuse trained models.
- Visualize logs and predictions with Grafana (optional/future).
- Automatically run on every code push or PR.

## 🚀 How It Works:

This project is powered by a two-stage GitHub Actions pipeline:

1. build job

   - Installs dependencies.
   - Collects system logs into logs/system_logs.txt.
   - Uploads logs as an artifact for the next job.

2. process_logs job
   - Downloads logs.
   - Cleans them via scripts/preprocess_logs.py.
   - Trains a model using scripts/train_model.py.
   - Makes a failure prediction using scripts/predict_failure.py.

## 📂 Project Structure:

📦ai-cicd
┣ 📂app/
┃ ┗ 📜main.py ← Sample app logic (can be empty)
┣ 📂logs/
┃ ┣ 📜system_logs.txt ← Collected logs
┃ ┣ 📜cleaned_logs.txt ← Processed logs
┣ 📂models/
┃ ┣ 📜failure_predictor.pkl ← Saved ML model
┃ ┗ 📜vectorizer.pkl ← TF-IDF vectorizer
┣ 📂scripts/
┃ ┣ 📜preprocess_logs.py ← Cleans and extracts useful logs
┃ ┣ 📜train_model.py ← Trains the AI model
┃ ┣ 📜predict_failure.py ← Runs prediction based on logs
┣ 📜.github/workflows/ai-cicd.yml ← GitHub Actions pipeline
┣ 📜requirements.txt
┗ 📜README.md / README.txt

## 🛠️ Getting Started:

1. Clone the repository
   git clone https://github.com/Gaurav896260/CI-CD-Failure-AI.git
   cd CI-CD-Failure-AI

2. Set up a virtual environment
   python -m venv venv
   source venv/bin/activate # on Linux/macOS
   venv\Scripts\activate # on Windows

3. Install requirements
   pip install -r requirements.txt

4. Run manually for local test
   python scripts/preprocess_logs.py
   python scripts/train_model.py
   python scripts/predict_failure.py

5. Trigger GitHub Actions
   Make a small change and push to GitHub:
   echo "# Trigger $(date)" >> README.md
   git add README.md
   git commit -m "🔁 Test CI/CD"
   git push

6. Monitor in GitHub
   Go to the Actions tab, open the latest workflow run.
   Look for:
   🔹 Found X failure logs and Y success logs.
   ✅ Model trained and saved!
   🧠 Prediction: 🚨 Likely to FAIL

## 🧠 Technologies Used:

- CI/CD: GitHub Actions
- ML: Scikit-learn, RandomForest
- Log Processing: Python + TF-IDF
- Storage: Local filesystem (logs, models)
- Optional: PostgreSQL, Elasticsearch, Grafana for visualization

## 📈 Future Enhancements:

- Improve prediction accuracy with more diverse CI/CD logs.
- Add Slack or email alert integrations.
- Auto-deploy or halt pipeline based on model prediction.
- Extend to Jenkins, GitLab CI/CD, CircleCI, etc.
- Add Grafana dashboard for real-time monitoring.

## 📬 Questions or Issues?

Feel free to open an issue on the GitHub repo or reach out for help setting it up!
