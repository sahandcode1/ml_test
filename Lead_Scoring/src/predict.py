from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd
from fastapi import FastAPI
from business_rules import apply_business_rules
from pydantic import BaseModel

app = FastAPI()

model = joblib.load(r"\git hub\ml_test\Lead_Scoring\model.pkl")

class Customer(BaseModel):
    age: int
    total_purchases: int
    last_interaction_days: int


@app.post("/predict")
def predict(customer: Customer):
    df = pd.DataFrame([customer.dict()])
    df = df[model.feature_names_in_]

    prediction = model.predict(df)[0]
    final_score = apply_business_rules(customer.dict(), prediction)

    return {
        'predicted_purchase': bool(final_score),
        'model_prediction': bool(prediction)
    }