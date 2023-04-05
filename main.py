from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

class Employee(BaseModel):
    YearsAtCompany: int
    EmployeeSatisfaction: float
    Position: str
    Salary: int

app = FastAPI()

with open('rfmodel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post("/")
async def return_employee(employee: Employee):
    request_json = employee.dict()
    response_json = request_json
    df_data = {key:[request_json[key]] for key in request_json}
    df = pd.DataFrame(data=df_data)
    value = model.predict(df)[0]
    if value == 1:
        response_json["riskLevel"] = "High"
        response_json["warning"] = "The employee is at high risk of leaving company. Please take preventative measures"
    else:
        response_json["riskLevel"] = "Low"
        response_json["warning"] = "'The employee is at no risk of leaving the company'"
    return response_json