import pandas as pd
import joblib
from fastapi import FastAPI
from business_rules import apply_business_rules

app = FastAPI()

model = joblib.load(r"\git hub\ml_test\Lead_Scoring\model.pkl")

@app.post("/predict")
def predict(customer:dict):
    df = pd.DataFrame([customer])
    df = pd.get_dummies(df,columns=['region'])

    for col in ['region_Shiraz', 'region_Tabriz', 'region_Tehran','region_Isfahan','region_Mashhad']:
        if col not in df.columns:
            df[col] = 0
    
    prediction = model.predict(df)[0]

    final_score = apply_business_rules(customer,prediction)

    return{
        'predicted_purchase':bool(final_score),
        'model_prediction':bool(prediction)
    }