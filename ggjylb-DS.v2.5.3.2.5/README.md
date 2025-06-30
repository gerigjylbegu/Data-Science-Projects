# Stroke Prediction Project

## Overview

This project predicts the likelihood of a stroke based on patient data. It consists of:

1. **Data Analysis and Modeling (`stroke_notebook.ipynb`):**
   - Performed exploratory data analysis (EDA) on the stroke dataset.
   - Explored relationships between features (age, gender, hypertension, heart disease, marital status, work type, residence type, average glucose level, BMI, smoking status) and stroke occurrence.
   - Addressed class imbalance using SMOTE.
   - Built and evaluated machine learning models (e.g., XGBoost, Random Forest).
   - Evaluated models using accuracy, F1-score, precision, recall, and ROC-AUC.
   - Used SHAP values for model interpretation and feature importance.

2. **Web Application (`app/`):**
   - Developed a Python web app to serve the trained stroke prediction model.
   - Users can input patient data and receive a stroke risk prediction.

## How to Use the App with Docker

### Prerequisites

- [Docker](https://www.docker.com/) installed on your system.

### Build and Run the Docker Container

1. **Build the Docker image:**

   From the root directory of the project, run:

   ```sh
   docker build -t stroke-app ./app
   ```

2. **Run the Docker container:**

   ```sh
   docker run -p 8000:8000 stroke-app
   ```

3. The app will be available at [http://localhost:8000](http://localhost:8000).

4. Use the web interface or API to input patient data and receive predictions.

### Required Input Features

- gender
- age
- hypertension
- heart_disease
- ever_married
- work_type
- Residence_type
- avg_glucose_level
- bmi
- smoking_status

Refer to the app interface for input format details.

## Project Structure

- `stroke_notebook.ipynb`: Data analysis, modeling, and interpretation.
- `healthcare-dataset-stroke-data.csv`: Dataset used to train the model.
- `functions.py`: Utility functions used in the notebook.
- `app/main.py`: Web app entry point.
- `app/model.py`: Model loading and prediction logic.
- `app/stroke_model.pkl`: Trained model file.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker configuration for the app.

## Achievements

- Developed a satisfactory, interpretable model to predict the probability of a patient having a stroke.
- Provided insights into key stroke risk factors using SHAP analysis.
- Deployed the model as a user-friendly web application using Docker.