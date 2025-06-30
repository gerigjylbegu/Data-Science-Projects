import pickle
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn import set_config

set_config(transform_output="pandas")

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/stroke_model.pkl", "rb") as f:
    model = pickle.load(f)


def predict(data):
    return "sroke" if model.predict(data)[0] == 1 else "no stroke"


def predict_proba(data):
    return model.predict_proba(data)[0][1]
