
# System Modules
import sys
import os
import math
 
# Installed Modules
import pytest
 
# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402
 
 
# ==================== area_of_circle ====================
 
def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1
 
    # Act
    result = area_of_circle(radius)
 
    # Assert
    assert abs(result - 3.14159) < 1e-5
 
 
def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0
 
    # Act
    result = area_of_circle(radius)
 
    # Assert
    assert result == 0
 
 
def test_area_of_circle_large_radius():
    """Test with a large radius."""
    # Arrange
    radius = 100
 
    # Act
    result = area_of_circle(radius)
 
    # Assert
    assert abs(result - math.pi * 10000) < 1e-5
 
 
def test_area_of_circle_decimal_radius():
    """Test with a decimal radius."""
    # Arrange
    radius = 2.5
 
    # Act
    result = area_of_circle(radius)
 
    # Assert
    assert abs(result - math.pi * 6.25) < 1e-5
 
 
def test_area_of_circle_negative_radius():
    """Test that a negative radius raises ValueError."""
    # Arrange
    radius = -1
 
    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(radius)
 
 
def test_area_of_circle_type_error():
    """Test that a non-numeric radius raises TypeError."""
    # Arrange
    radius = "five"
 
    # Act & Assert
    with pytest.raises(TypeError):
        area_of_circle(radius)
 
 
# ==================== get_nth_fibonacci ====================
 
def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0
 
    # Act
    result = get_nth_fibonacci(n)
 
    # Assert
    assert result == 0
 
 
def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1
 
    # Act
    result = get_nth_fibonacci(n)
 
    # Assert
    assert result == 1
 
 
def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10
 
    # Act
    result = get_nth_fibonacci(n)
 
    # Assert
    assert result == 55
 
 
def test_get_nth_fibonacci_two():
    """Test with n=2."""
    # Arrange
    n = 2
 
    # Act
    result = get_nth_fibonacci(n)
 
    # Assert
    assert result == 1
 
 
def test_get_nth_fibonacci_twenty():
    """Test with n=20."""
    # Arrange
    n = 20
 
    # Act
    result = get_nth_fibonacci(n)
 
    # Assert
    assert result == 6765
 
 
def test_get_nth_fibonacci_negative():
    """Test that a negative n raises ValueError."""
    # Arrange
    n = -5
 
    # Act & Assert
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(n)
 
 
def test_get_nth_fibonacci_type_error():
    """Test that a non-integer n raises TypeError."""
    # Arrange
    n = "ten"
 
    # Act & Assert
    with pytest.raises(TypeError):
        get_nth_fibonacci(n)
 
 
@pytest.mark.parametrize("n, expected", [
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
])
def test_get_nth_fibonacci_parametrize(n, expected):
    """Test multiple Fibonacci values using parametrize."""
    # Act
    result = get_nth_fibonacci(n)
 
    # Assert
    assert result == expected