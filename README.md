# 🎓 Student Exam Performance Predictor

An end-to-end **Machine Learning web application** that predicts a student’s **Maths score** based on demographic information, academic background, and preparation level.  
The project demonstrates how a trained ML model can be deployed as a **production-ready Flask web application**.

---

## 🚀 Live Demo

🔗 **Deployed Application**:  
https://student-performance-indicator-0w7h.onrender.com

---

## 📌 Project Overview

This project is designed to showcase:
- Complete Machine Learning lifecycle
- Modular coding practices
- Model serialization and reuse
- Web-based inference using Flask
- Clean and interactive UI

The application takes user inputs through a web form and returns a real-time prediction using a trained regression model.

---

## 🧠 Problem Statement

Given a student’s:
- Gender  
- Race / Ethnicity  
- Parental level of education  
- Lunch type  
- Test preparation status  
- Reading score  
- Writing score  

Predict the **Maths score** using a Machine Learning model.

---

## 🏗️ Project Architecture

├── ./
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
│   ├── tree.py
│   ├── logs/
│   │   ├── 01_20_2026_22_47_14.log
│   ├── ML_Project.egg-info/
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── requires.txt
│   │   ├── SOURCES.txt
│   │   ├── top_level.txt
│   ├── Notebook/
│   │   ├── EDA.ipynb
│   │   ├── model_training.ipynb
│   │   ├── data/
│   │   │   ├── stud.csv
│   ├── src/
│   │   ├── exception.py
│   │   ├── logger.py
│   │   ├── utils.py
│   │   ├── __init__.py
│   │   ├── components/
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_transformation.py
│   │   │   ├── model_trainer.py
│   │   │   ├── __init__.py
│   │   ├── pipeline/
│   │   │   ├── predict_pipeline.py
│   │   │   ├── train_pipeline.py
│   │   │   ├── __init__.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── index.html



---

## ⚙️ Tech Stack

### 🔹 Programming & Libraries
- Python
- NumPy
- Pandas
- Scikit-learn

### 🔹 Web Framework
- Flask
- Gunicorn

### 🔹 Machine Learning
- Linear Regression
- Data Preprocessing Pipelines
- OneHotEncoder
- StandardScaler
- ColumnTransformer

### 🔹 Deployment
- Render (Cloud Hosting)

---

## 🧩 Machine Learning Pipeline

1. **Data Ingestion**
   - Raw dataset loading
2. **Data Transformation**
   - Categorical encoding
   - Numerical scaling
3. **Model Training**
   - Multiple regression models tested
   - Best model selected using R² score
4. **Serialization**
   - Model and preprocessor saved using Pickle
5. **Inference**
   - Same preprocessor reused during prediction to ensure consistency

---

## 🖥️ Web Application Flow

1. User lands on a **Landing Page** (`/`)
2. Redirects to the **Prediction Page** (`/predictdata`)
3. User fills the form
4. Flask backend:
   - Converts inputs to DataFrame
   - Applies preprocessing
   - Runs model inference
5. Predicted Maths score is displayed on the UI


