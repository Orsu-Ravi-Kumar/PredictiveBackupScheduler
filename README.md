🧠 Predictive Backup Scheduler (AI + SQL Server + FastAPI + Docker)
A machine learning-powered backup recommendation engine that predicts the optimal time to perform SQL Server backups based on historical workload and performance metrics.
---
🚀 Project Overview
Traditional backup jobs run at fixed schedules, ignoring server load, query performance, or previous backup failures. This project solves that by using **machine learning to predict risky backup times** and offering a real-time **API recommendation engine**.
> 📌 Goal: Prevent slow, failed, or disruptive backups by intelligently scheduling them during low-risk periods.
---
🧱 Tech Stack
- SQL Server (Backupset + Query Stats)
- Python 3.10, Pandas, Scikit-learn
- FastAPI m(REST API Framework)
- Docker (Containerized Deployment)
- Uvicorn (ASGI Server)
- (Optional: Azure Functions / Container Apps)
---
## 📊 ML Model Overview
- Input Features:
  - hour: Hour of the day
  - day_of_week: Weekday (0=Monday)
  - backup_size: Backup size in bytes
- Label:
  - failure_risk: 1 = risky (slow/failure), 0 = safe
Trained using **Random Forest Classifier** on synthetic and real backup logs.
---
📁 Project Structure
Predictive-Backup-Scheduler/
├── data/ # backup_logs.csv, workload_metrics.csv
├── models/ # backup_predictor.pkl
├── scripts/ # feature_engineering.py, train_model.py
├── app/ # fastapi_app.py
├── deployment/
│ └── docker/ # Dockerfile
├── notebooks/ # Optional exploratory notebooks
├── requirements.txt
└── README.md


 📦 How to Run Locally

1. Clone this repo

bash
git clone https://github.com/<your-username>/Predictive-Backup-Scheduler.git
cd Predictive-Backup-Scheduler

--> Dependencies
pip install -r requirements.txt

--> Run Fast API app 
uvicorn app.fastapi_app:app --reload

🐳 Docker Support
1. Build Docker image
   
docker build -t backup-scheduler -f deployment/docker/Dockerfile .
2. Run the container

docker run -p 8000:80 backup-scheduler

Visit:
🔗 http://127.0.0.1:8000/docs

🧪 Example API Usage
Endpoint: /predict/
Method: GET

Example:
----------------------------------------
/predict?hour=2&day_of_week=0&backup_size=52428800
Returns:
---------------------------------------
{
  "hour": 2,
  "day_of_week": 0,
  "backup_size": 52428800,
  "prediction": 0,
  "recommendation": "Recommended"
}


🧠 Key Outcomes
✅ Predicts backup risks using AI

✅ Automates backup decision-making

✅ Containerized for cloud deployments

✅ Lightweight, scalable, and practical

📌 Use Cases
💡 Automate backup job scheduling intelligently

📉 Minimize failed or high-latency backups

🔄 Integrate with SQL Server Agent or Azure Logic Apps

☁️ Deploy to Azure for full-scale production use

📬 Author
Ravikumar Orsu
💼 SQL Server DBA | Azure Data Engineer | AI Integrator
🔗 [LinkedIn](https://www.linkedin.com/in/ravikumarorsu/)
