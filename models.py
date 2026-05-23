"""Pydantic models for request validation."""

from pydantic import BaseModel, Field
from typing import Literal


class Numbers(BaseModel):
    """Request model for calculator operations.
    
    Attributes:
        operation: Type of calculation to perform.
        numbers: List of numbers to perform operation on.
        base: Optional base parameter for logarithm calculations.
    """
    operation: Literal["sum", "product", "difference", "division", "log"] = Field(
        ..., description="Type of operation to perform"
    )
    numbers: list[float] = Field(..., description="List of numbers for the operation")
    base: float | None = Field(None, description="Optional base for logarithm (use with 'log' operation)")