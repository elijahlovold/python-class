import pytest
from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == 0  # First Fibonacci number
    assert fibonacci(1) == 1  # Second Fibonacci number
    assert fibonacci(5) == 5  # 5th Fibonacci number
    assert fibonacci(10) == 55  # 10th Fibonacci number
    assert fibonacci(15) == 610  # 15th Fibonacci number

