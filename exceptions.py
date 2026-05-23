"""Custom exception classes for calculator operations."""


class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class EmptyListError(CalculatorError):
    """Raised when an empty list is provided to a calculation."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass


class LogarithmError(CalculatorError):
    """Raised when invalid logarithm parameters are provided."""
    pass
