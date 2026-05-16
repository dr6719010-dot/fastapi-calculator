from fastapi import FastAPI, HTTPException
from calculator import (
    calculate_sum,
    calculate_product,
    calculate_difference,
    calculate_division
)
from models import Numbers

app = FastAPI()

# Dict pattern - maps operation name to function
operations = {
    "sum": calculate_sum,
    "product": calculate_product,
    "difference": calculate_difference,
    "division": calculate_division
}

@app.get("/")
def home():
    return {"message": "Calculator API is live 🚀"}

@app.post("/calculate")
def calculate(data: Numbers):
    operation = operations[data.operation]
    result = operation(data.numbers)
    return {"operation": data.operation, "result": result}