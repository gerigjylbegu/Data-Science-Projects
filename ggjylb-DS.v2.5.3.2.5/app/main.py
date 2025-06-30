import fastapi
import pandas as pd
from model import predict, predict_proba
from pydantic import BaseModel, validator
from typing import Optional, Literal

app = fastapi.FastAPI()


class StrokeInput(BaseModel):
    gender: Literal["Male", "Female", "Other"]
    age: float
    hypertension: Literal[0, 1]
    heart_disease: Literal[0, 1]
    ever_married: Literal["Yes", "No"]
    work_type: Literal[
        "children", "Govt_job", "Never_worked", "Private", "Self-employed"
    ]
    Residence_type: Literal["Rural", "Urban"]
    avg_glucose_level: float
    bmi: Optional[float] = None
    smoking_status: Literal["formerly smoked", "never smoked", "smokes", "Unknown"]

    @validator("age")
    def validate_age(cls, v):
        if v < 0 or v > 120:
            raise ValueError("Age must be between 0 and 120")
        return v

    @validator("avg_glucose_level")
    def validate_glucose(cls, v):
        if v < 50 or v > 300:
            raise ValueError("Average glucose level must be between 50 and 300")
        return v

    @validator("bmi")
    def validate_bmi(cls, v):
        if v is not None and (v < 10 or v > 100):
            raise ValueError("BMI must be between 10 and 100")
        return v


class StrokeResponse(BaseModel):
    prediction: str
    probability: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict", response_model=StrokeResponse)
async def predict_stroke(data: StrokeInput):
    try:
        input_dict = data.dict()
        df = pd.DataFrame([input_dict])
        prediction = predict(df)
        proba = predict_proba(df)

        return {"prediction": prediction, "probability": proba}

    except Exception as e:
        raise fastapi.HTTPException(
            status_code=500, detail=f"Prediction failed: {str(e)}"
        )
