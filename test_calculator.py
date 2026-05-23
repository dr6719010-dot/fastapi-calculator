"""Unit tests for calculator operations."""

import pytest
import math
from calculator import (
    calculate_sum,
    calculate_product,
    calculate_difference,
    calculate_division,
    logarithms,
    validate_numbers
)
from exceptions import (
    CalculatorError,
    EmptyListError,
    DivisionByZeroError,
    LogarithmError
)


class TestValidateNumbers:
    """Tests for number validation."""
    
    def test_validate_numbers_valid(self):
        """Test validation with valid numbers."""
        nums = [1, 2, 3]
        result = validate_numbers(nums)
        assert result == [1, 2, 3]
    
    def test_validate_numbers_none(self):
        """Test validation with None."""
        with pytest.raises(CalculatorError, match="numbers are required"):
            validate_numbers(None)
    
    def test_validate_numbers_empty(self):
        """Test validation with empty list."""
        with pytest.raises(EmptyListError, match="numbers list cannot be empty"):
            validate_numbers([])


class TestSum:
    """Tests for sum operation."""
    
    def test_sum_positive(self):
        """Test sum with positive numbers."""
        assert calculate_sum([1, 2, 3]) == 6
    
    def test_sum_negative(self):
        """Test sum with negative numbers."""
        assert calculate_sum([-1, -2, -3]) == -6
    
    def test_sum_mixed(self):
        """Test sum with mixed numbers."""
        assert calculate_sum([10, -5, 3]) == 8
    
    def test_sum_floats(self):
        """Test sum with floating point numbers."""
        assert calculate_sum([1.5, 2.5, 1.0]) == 5.0
    
    def test_sum_empty(self):
        """Test sum with empty list."""
        with pytest.raises(EmptyListError):
            calculate_sum([])


class TestProduct:
    """Tests for product operation."""
    
    def test_product_positive(self):
        """Test product with positive numbers."""
        assert calculate_product([2, 3, 4]) == 24
    
    def test_product_with_zero(self):
        """Test product with zero."""
        assert calculate_product([2, 0, 3]) == 0
    
    def test_product_negative(self):
        """Test product with negative numbers."""
        assert calculate_product([-2, 3, 4]) == -24
    
    def test_product_single(self):
        """Test product with single number."""
        assert calculate_product([5]) == 5
    
    def test_product_empty(self):
        """Test product with empty list."""
        with pytest.raises(EmptyListError):
            calculate_product([])


class TestDifference:
    """Tests for difference operation."""
    
    def test_difference_basic(self):
        """Test basic difference."""
        assert calculate_difference([10, 3, 2]) == 5
    
    def test_difference_negative_result(self):
        """Test difference with negative result."""
        assert calculate_difference([5, 10]) == -5
    
    def test_difference_single(self):
        """Test difference with single number."""
        assert calculate_difference([7]) == 7
    
    def test_difference_multiple(self):
        """Test difference with multiple numbers."""
        assert calculate_difference([100, 25, 15, 10]) == 50


class TestDivision:
    """Tests for division operation."""
    
    def test_division_basic(self):
        """Test basic division."""
        assert calculate_division([10, 2]) == 5
    
    def test_division_multiple(self):
        """Test division with multiple numbers."""
        assert calculate_division([100, 2, 5]) == 10
    
    def test_division_by_zero(self):
        """Test division by zero error."""
        with pytest.raises(DivisionByZeroError, match="division by zero is not allowed"):
            calculate_division([10, 0])
    
    def test_division_by_zero_second_divisor(self):
        """Test division by zero in second divisor."""
        with pytest.raises(DivisionByZeroError):
            calculate_division([10, 2, 0])
    
    def test_division_insufficient_numbers(self):
        """Test division with only one number."""
        with pytest.raises(CalculatorError, match="division requires at least 2 numbers"):
            calculate_division([10])
    
    def test_division_insufficient_numbers_empty(self):
        """Test division with empty list."""
        with pytest.raises(EmptyListError):
            calculate_division([])


class TestLogarithms:
    """Tests for logarithm operation."""
    
    def test_logarithm_natural(self):
        """Test natural logarithm."""
        result = logarithms([1, 2.718281828])
        assert result[0] == pytest.approx(0, abs=1e-5)
        assert result[1] == pytest.approx(1, abs=1e-5)
    
    def test_logarithm_base_10(self):
        """Test logarithm with base 10."""
        result = logarithms([1, 10, 100], base=10)
        assert result[0] == pytest.approx(0, abs=1e-5)
        assert result[1] == pytest.approx(1, abs=1e-5)
        assert result[2] == pytest.approx(2, abs=1e-5)
    
    def test_logarithm_negative_number(self):
        """Test logarithm with negative number."""
        with pytest.raises(LogarithmError, match="logarithm is only defined for positive numbers"):
            logarithms([-1, 2, 3])
    
    def test_logarithm_zero(self):
        """Test logarithm with zero."""
        with pytest.raises(LogarithmError, match="logarithm is only defined for positive numbers"):
            logarithms([0, 1, 2])
    
    def test_logarithm_invalid_base_zero(self):
        """Test logarithm with base 0."""
        with pytest.raises(LogarithmError, match="base must be positive"):
            logarithms([1, 2], base=0)
    
    def test_logarithm_invalid_base_negative(self):
        """Test logarithm with negative base."""
        with pytest.raises(LogarithmError, match="base must be positive"):
            logarithms([1, 2], base=-1)
    
    def test_logarithm_base_one(self):
        """Test logarithm with base 1."""
        with pytest.raises(LogarithmError, match="base cannot be 1"):
            logarithms([1, 2], base=1)
