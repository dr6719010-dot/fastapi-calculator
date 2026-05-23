"""FastAPI calculator application with history tracking and logging."""

import logging
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Calculator API", version="1.0.0")

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

# In-memory history storage (last 50 calculations)
calculation_history: list[dict] = []
MAX_HISTORY_SIZE = 50

@app.get("/", tags=["Health"])
def home():
    """Health check endpoint."""
    logger.info("Health check called")
    return {"message": "Calculator API is live 🚀"}


@app.get("/history", tags=["History"])
def get_history():
    """Get calculation history (last 50 calculations)."""
    logger.info(f"History requested - {len(calculation_history)} calculations stored")
    return {"history": calculation_history, "total_calculations": len(calculation_history)}

@app.post("/calculate", tags=["Operations"])
def calculate(data: Numbers):
    """Execute a calculation operation.
    
    Args:
        data: Numbers model containing operation, numbers list, and optional base.
    
    Returns:
        Dictionary with operation, result, and timestamp.
    
    Raises:
        HTTPException: For invalid operations or calculation errors.
    """
    logger.info(f"Calculate request: operation={data.operation}, numbers_count={len(data.numbers)}")
    
    # Validate operation
    if data.operation not in operations:
        logger.warning(f"Invalid operation requested: {data.operation}")
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid operation. Must be one of: {', '.join(operations.keys())}"
        )
    
    try:
        operation = operations[data.operation]
        result = operation(data.numbers, data.base)
        
        # Create history entry
        history_entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": data.operation,
            "numbers": data.numbers,
            "base": data.base,
            "result": result
        }
        
        # Store in history
        calculation_history.append(history_entry)
        if len(calculation_history) > MAX_HISTORY_SIZE:
            calculation_history.pop(0)
        
        logger.info(f"Calculation successful: {data.operation} = {result}")
        return {"operation": data.operation, "result": result, "timestamp": history_entry["timestamp"]}
        
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
        logger.exception(f"Unexpected error during calculation: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
