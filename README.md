# 🎓 Early Student Success Platform

> **An end-to-end MLOps platform that predicts student dropout risk, explains contributing factors using Explainable AI, and recommends personalized interventions to improve student retention.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![AWS](https://img.shields.io/badge/AWS-Deployment-yellow)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

# 📖 Overview

Student dropout is a major challenge for universities worldwide. Most institutions identify struggling students only after academic performance has significantly declined.

The **Early Student Success Platform** is designed to help institutions detect at-risk students **before** they leave college.

Instead of only predicting whether a student may drop out, the platform also explains **why** the student is at risk and suggests actionable interventions such as:

- Academic tutoring
- Attendance monitoring
- Financial aid review
- Advisor meetings
- Counseling support

This project demonstrates a complete **Machine Learning Engineering + MLOps** workflow from raw data ingestion to cloud deployment.

---

# 🚀 Features

- End-to-end Machine Learning Pipeline
- Automated Data Validation
- Data Cleaning Pipeline
- Feature Engineering
- Model Training
- Hyperparameter Optimization (Optuna)
- Experiment Tracking (MLflow)
- Explainable AI (SHAP)
- Student Risk Prediction API
- Batch Prediction
- Docker Deployment
- AWS Deployment
- CI/CD with GitHub Actions
- Unit Testing
- Modular Production Architecture

---

# 🏗 Project Architecture

```text
                  Raw Dataset
                        │
                        ▼
              Data Validation Pipeline
                        │
                        ▼
                Data Cleaning Pipeline
                        │
                        ▼
             Feature Engineering Pipeline
                        │
                        ▼
                  Model Training
          (LightGBM / XGBoost / CatBoost)
                        │
                        ▼
              Hyperparameter Optimization
                     (Optuna)
                        │
                        ▼
               Experiment Tracking
                    (MLflow)
                        │
                        ▼
                 Registered Model
                        │
                        ▼
                 FastAPI Inference API
                        │
                        ▼
               Docker Container
                        │
                        ▼
                 AWS Cloud Deployment
                        │
                        ▼
             Student Risk Predictions
                        │
                        ▼
             SHAP Explanations
                        │
                        ▼
        Personalized Intervention Suggestions
```

---

# 📂 Repository Structure

```text
Early-Student-Success-Platform/

├── artifacts/
├── configs/
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── mlruns/
├── models/
├── notebooks/
├── src/
│   ├── api/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── utils/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── README.md
├── requirements.txt
└── .github/workflows/
```

---

# 🧠 Machine Learning Workflow

The pipeline consists of the following stages:

1. Data Ingestion
2. Data Validation
3. Data Cleaning
4. Feature Engineering
5. Model Training
6. Hyperparameter Optimization
7. Model Evaluation
8. Explainability (SHAP)
9. Deployment
10. Monitoring

---

# 📊 Models

The following models are compared:

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM
- CatBoost

The best-performing model is automatically selected based on evaluation metrics and registered with MLflow.

---

# 📈 Evaluation Metrics

The platform evaluates models using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- PR-AUC
- Confusion Matrix
- Calibration Curve

---

# 🔍 Explainable AI

Instead of returning only a prediction probability, the platform also provides feature-level explanations using SHAP.

Example output:

```json
{
    "student_id": 1042,
    "dropout_probability": 0.91,
    "risk_level": "High",
    "top_reasons": [
        "Attendance below 60%",
        "Declining GPA",
        "Outstanding tuition balance"
    ],
    "recommended_actions": [
        "Schedule tutoring",
        "Meet academic advisor",
        "Financial aid consultation"
    ]
}
```

---

# 🌐 REST API

Example endpoints:

```
POST /predict

POST /batch_predict

GET /health

GET /model_info

GET /metrics
```

Interactive API documentation is automatically available through Swagger UI.

---

# 🐳 Docker

Build:

```bash
docker build -t student-success .
```

Run:

```bash
docker run -p 8000:8000 student-success
```

---

# ☁ AWS Deployment

Deployment options:

- AWS Lambda
- API Gateway
- ECS Fargate
- EC2

The repository includes Docker support for cloud deployment.

---

# 🧪 Testing

Run:

```bash
pytest
```

The project includes:

- Unit Tests
- API Tests
- Model Tests
- Data Validation Tests

---

# 📚 Tech Stack

### Machine Learning

- Scikit-Learn
- LightGBM
- XGBoost
- CatBoost
- Optuna

### MLOps

- MLflow
- Docker
- GitHub Actions

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Explainability

- SHAP

### Cloud

- AWS

---

# 📌 Future Improvements

- Real-time monitoring
- Data drift detection
- Model retraining pipeline
- Student analytics dashboard
- Role-based authentication
- PostgreSQL integration
- Feature Store
- Kubernetes deployment

---

# 👨‍💻 Author

Built as a production-grade Machine Learning Engineering project demonstrating modern MLOps practices, scalable deployment, and explainable AI for educational analytics.

---
