# 🛡️ Fraud Detection System with AWS

A real-time fraud detection system that uses machine learning models deployed via FastAPI and hosted on AWS EC2, with scalable data handling through AWS S3. Built for high accuracy and fast inference in production.

---

## 🚀 Features

- ⚡ **Real-time fraud prediction** API using FastAPI
- 🧠 **Machine Learning models** trained with XGBoost and LightGBM
- 📈 **Model performance**:  
  - ROC AUC: 0.9458  
  - True Positive Rate: 97.72%  
  - Specificity: 90.16%
- ☁️ **Cloud Deployment** on AWS EC2
- 📦 **Data storage** and management via AWS S3
- 📊 Preprocessing pipeline with balanced class weights and outlier filtering

---

## 🧠 Model Training

Trained on anonymized transaction data using:
- `XGBoost` for ensemble classification
- `LightGBM` for comparison and optimization
- Custom metrics: Precision, Recall, ROC AUC, Specificity, TPR

---

## 🧪 API Usage

Deployed using **FastAPI**, allowing quick fraud checks via POST requests.

### Example request:
```json
POST /predict
{
  "amount": 112.00,
  "oldbalanceOrg": 100.00,
  "newbalanceOrig": 0.00
}
```

### Example response:
```json
{
  "is_fraud": true,
  "confidence": 0.978
}
```

---

## 📁 Project Structure

```
.
├── api/                  # FastAPI app
│   ├── main.py           # API endpoints
│   └── model.pkl         # Trained ML model
├── training/             # Model training scripts
│   └── train.py
├── requirements.txt
├── README.md
└── .env (ignored)
```

---

## 🔐 Environment Variables

| Key              | Description                       |
|------------------|-----------------------------------|
| `AWS_ACCESS_KEY` | AWS key for S3 access (if needed) |
| `AWS_SECRET_KEY` | AWS secret                        |

> ⚠️ Never commit `.env` or keys to public repos.

---

## 🧠 Technologies Used

- Python
- FastAPI
- XGBoost & LightGBM
- AWS EC2 & S3
- scikit-learn
- pandas / numpy

---

## 📜 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

---

## 📌 Credits

Developed by [Sparsh Guha](https://github.com/SG7504)
