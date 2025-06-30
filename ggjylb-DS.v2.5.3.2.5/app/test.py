import pickle
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn import set_config
import os
os.environ["PYTHONWARNINGS"] = "ignore::ConvergenceWarning,ignore::FutureWarning"


set_config(transform_output="pandas")

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/stroke_model.pkl", "rb") as f:
    model = pickle.load(f)


data = {
  "gender": "Male",
  "age": 67,
  "hypertension": 1,
  "heart_disease": 0,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Rural",
  "avg_glucose_level": 200,
  "bmi": 32,
  "smoking_status": "formerly smoked"
}

df = pd.DataFrame([data])

a = model.predict_proba(df)

print(a[0][1])