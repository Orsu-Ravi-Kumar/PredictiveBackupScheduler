import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load features
df = pd.read_csv("C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/data/features.csv")

# Features and label
X = df[['hour', 'day_of_week', 'backup_size']]
y = df['failure_risk']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/models/backup_predictor.pkl")
print("✅ Model saved to models/backup_predictor.pkl")
