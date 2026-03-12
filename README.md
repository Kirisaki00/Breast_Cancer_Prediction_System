# Breast Cancer Tumor Stage Prediction System

A **Machine Learning based web application** that predicts the **tumor stage of breast cancer** using clinical and genetic features.
The system is built using **Scikit-Learn, Flask, and Render**, and provides an interactive web interface for making predictions.

---

## Live Demo

🔗 https://breast-cancer-prediction-system-zc36.onrender.com/

## GitHub Repository

🔗 https://github.com/Kirisaki00/Breast_Cancer_Prediction_System

---

# Project Overview

This project demonstrates a **complete end-to-end machine learning workflow**:

1. Data preprocessing and feature selection
2. Training a machine learning classification model
3. Exporting the trained model
4. Building a Flask API for predictions
5. Creating a web interface for user input
6. Deploying the application on the cloud

Users can input clinical and biological features and the system predicts the **breast cancer tumor stage with probability scores**.

---

# Features

* Predicts **Breast Cancer Tumor Stage**
* Uses **clinical and gene expression data**
* Displays **prediction confidence**
* Shows **probability breakdown for each tumor stage**
* Interactive **web UI for easy input**
* Fully **deployed ML web application**

---

# Tech Stack

## Machine Learning

* Python
* Scikit-Learn
* Pandas
* NumPy

## Backend

* Flask
* Gunicorn

## Frontend

* HTML
* CSS
* JavaScript

## Deployment

* Render

---

# Model Information

The model used in this project is:

**Random Forest Classifier**

Random Forest works well for **tabular medical datasets** and provides robust predictions by combining multiple decision trees.

### Features Used

The model uses the following features:

* Nottingham Prognostic Index
* Tumor Size
* Lymph Nodes Examined Positive
* Chemotherapy
* Hormone Therapy
* Neoplasm Histologic Grade
* Radio Therapy
* Age at Diagnosis
* ER Status
* HER2 Status
* Menopausal State
* AURKA Gene Expression

These features are converted into a structured input vector and passed into the trained model for prediction.

---

# Application Interface

The web interface allows users to:

* Enter patient clinical information
* Select receptor status
* Provide treatment history
* Run prediction
* View tumor stage and probability breakdown

Example prediction output:

* **Predicted Stage:** Stage II
* **Model Confidence:** 62.6%
* **Probability Breakdown:**

  * Stage I
  * Stage II
  * Stage III

---

# Screenshot

<img width="1773" height="988" alt="image" src="https://github.com/user-attachments/assets/9bd04a2b-6261-4cb9-8224-9456b7343a48" />

---

# Project Structure

```
Breast_Cancer_Prediction_System
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
│
├── templates
│   └── index.html
│
├── Dataset
│   └── METABRIC_RNA_Mutation.csv
│
└── BreastCancerPrediction.ipynb
```

---

# Installation

Clone the repository

```
git clone https://github.com/Kirisaki00/Breast_Cancer_Prediction_System.git
cd Breast_Cancer_Prediction_System
```

Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running Locally

Start the Flask server

```
python app.py
```

Open in browser

```
http://localhost:5000
```

---

# API Endpoints

## Health Check

```
GET /healthcheck
```

Response example

```
{
  "status": "ok",
  "model": "RandomForestClassifier"
}
```

---

## Prediction Endpoint

```
POST /predict
```

Example request

```
{
 "nottingham_prognostic_index":3.2,
 "tumor_size":25,
 "lymph_nodes_examined_positive":2,
 "chemotherapy":1,
 "hormone_therapy":1,
 "neoplasm_histologic_grade":2,
 "radio_therapy":1,
 "age_at_diagnosis":55,
 "er_status":"Positive",
 "her2_status":"Negative",
 "inferred_menopausal_state":"Post",
 "aurka":3.4
}
```

---

# Deployment

This application is deployed using **Render**.

Deployment steps:

1. Push the project to GitHub
2. Connect the repository to Render
3. Configure build command

```
pip install -r requirements.txt
```

4. Configure start command

```
gunicorn app:app
```

Render automatically redeploys the application whenever new changes are pushed to GitHub.

---

# Dataset

The model is trained using the **METABRIC (Molecular Taxonomy of Breast Cancer International Consortium)** dataset containing clinical and genomic information from breast cancer patients.

---

# Future Improvements

* Add **model explainability (SHAP values)**
* Improve **UI with modern frameworks**
* Add **multiple ML models for comparison**
* Add **Docker containerization**
* Implement **CI/CD pipeline**
* Add **prediction visualizations**

---

# Author

**Kirisaki**

GitHub
https://github.com/Kirisaki00
