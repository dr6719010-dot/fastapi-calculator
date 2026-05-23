"""Calculator core logic module.

Provides functions for basic and advanced mathematical operations
with proper validation and error handling.
"""

from exceptions import CalculatorError, EmptyListError, DivisionByZeroError, LogarithmError
import math


def validate_numbers(nums: list[float]) -> list[float]:
    """Validate that numbers list is not None and not empty.
    
    Args:
        nums: List of numbers to validate.
    
    Returns:
        The validated numbers list.
    
    Raises:
        CalculatorError: If nums is None.
        EmptyListError: If nums list is empty.
    """
    if nums is None:
        raise CalculatorError("numbers are required")
    if len(nums) == 0:
        raise EmptyListError("numbers list cannot be empty")
    return nums


def calculate_sum(nums: list[float], base: float | None = None) -> float:
    """Calculate the sum of numbers.
    
    Args:
        nums: List of numbers to sum.
        base: Unused parameter for API consistency.
    
    Returns:
        Sum of all numbers.
    """
    nums = validate_numbers(nums)
    return sum(nums)


def calculate_product(nums: list[float], base: float | None = None) -> float:
    """Calculate the product of numbers.
    
    Args:
        nums: List of numbers to multiply.
        base: Unused parameter for API consistency.
    
    Returns:
        Product of all numbers.
    """
    nums = validate_numbers(nums)
    result = 1
    for n in nums:
        result *= n
    return result


def calculate_difference(nums: list[float], base: float | None = None) -> float:
    """Calculate the difference (first number minus all others).
    
    Args:
        nums: List of numbers. First is minuend, rest are subtrahends.
        base: Unused parameter for API consistency.
    
    Returns:
        Result of subtracting all numbers from the first.
    """
    nums = validate_numbers(nums)
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result


def calculate_division(nums: list[float], base: float | None = None) -> float:
    """Calculate the division (first number divided by all others).
    
    Args:
        nums: List of numbers. First is dividend, rest are divisors.
        base: Unused parameter for API consistency.
    
    Returns:
        Result of dividing first number by all others sequentially.
    
    Raises:
        CalculatorError: If fewer than 2 numbers provided.
        DivisionByZeroError: If any divisor is zero.
    """
    nums = validate_numbers(nums)
    if len(nums) < 2:
        raise CalculatorError("division requires at least 2 numbers")
    if 0 in nums[1:]:
        raise DivisionByZeroError("division by zero is not allowed")
    result = nums[0]
    for n in nums[1:]:
        result /= n
    return result

def logarithms(nums: list[float], base: float | None = None) -> list[float]:
    """Calculate logarithm of each number.
    
    Args:
        nums: List of positive numbers to take logarithm of.
        base: Base for logarithm. If None, uses natural logarithm.
    
    Returns:
        List of logarithm values.
    
    Raises:
        LogarithmError: If any number is <= 0, or base is invalid.
    """
    nums = validate_numbers(nums)

    for n in nums:
        if n <= 0:
            raise LogarithmError(
                "logarithm is only defined for positive numbers"
            )

    if base is not None:
        if base <= 0:
            raise LogarithmError("base must be positive")
        if base == 1:
            raise LogarithmError("base cannot be 1")
        return [math.log(n, base) for n in nums]

    return [math.log(n) for n in nums]
