"""FastAPI calculator application with history tracking and logging."""

import logging
from database import create_table, save_calculation, get_history
from datetime import datetime
from exceptions import CalculatorError, EmptyListError, DivisionByZeroError, LogarithmError
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from calculator import (
    calculate_sum,
    calculate_product,
    calculate_difference,
    calculate_division,
    logarithms
)
from models import Numbers

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="CalcX API", version="1.0.0")
create_table()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

operations = {
    "sum": calculate_sum,
    "product": calculate_product,
    "difference": calculate_difference,
    "division": calculate_division,
    "log": logarithms
}

@app.get("/", tags=["Health"])
def home():
    """Health check endpoint."""
    logger.info("Health check called")
    return {"message": "CalcX API is live 🚀"}

@app.get("/history", tags=["History"])
def history():
    """Get calculation history from database."""
    data = get_history()
    logger.info(f"History requested - {len(data)} calculations found")
    return {"history": data, "total_calculations": len(data)}

@app.post("/calculate", tags=["Operations"])
def calculate(data: Numbers):
    """Execute a calculation operation."""
    logger.info(f"Calculate request: operation={data.operation}, numbers_count={len(data.numbers)}")

    if data.operation not in operations:
        logger.warning(f"Invalid operation requested: {data.operation}")
        raise HTTPException(
            status_code=400,
            detail=f"Invalid operation. Must be one of: {', '.join(operations.keys())}"
        )

    try:
        operation = operations[data.operation]
        result = operation(data.numbers, data.base)
        save_calculation(data.operation, result)
        logger.info(f"Calculation successful: {data.operation} = {result}")
        return {
            "operation": data.operation,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
    except EmptyListError as e:
        logger.error(f"Empty list error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except DivisionByZeroError as e:
        logger.error(f"Division by zero error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except LogarithmError as e:
        logger.error(f"Logarithm error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except CalculatorError as e:
        logger.error(f"Calculator error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")