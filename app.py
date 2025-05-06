# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from preclampsia import PreclampsiaBase
import numpy as np
import pickle
import pandas as pd
import warnings
from fastapi.middleware.cors import CORSMiddleware
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

warnings.filterwarnings("ignore", message="X does not have valid feature names", category=UserWarning)
# 3. Index route, opens automatically on http://127.0.0.1:8000

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Preclampia Test': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_preclampsia(data:PreclampsiaBase):
    data = data.dict()
    age=data['Age']
    weight=data['Pre_pregnancy_Weight']
    income=data['Annual_Income']
    status=data['Socioeconomic_Status']
    history_hypertension=data['History_of_Hypertension']
    history_diabetes=data['History_of_Diabetes']
    history_preeclampsia=data['History_of_Preeclampsia']
    proteinuria_levels=data['Proteinuria_Levels']
    month=data['Month']
    systolic_bp=data['Systolic_BP']
    diastolic_bp=data['Diastolic_BP']
    parity=data['Parity']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[age,weight,parity,income,status,history_hypertension,
    history_diabetes,history_preeclampsia,proteinuria_levels,month,systolic_bp,
    diastolic_bp]])
    if(prediction[0] == 0):
        prediction="Low Risk of Preeclampsia"
    else:
        prediction="High Risk of Preeclampsia"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
