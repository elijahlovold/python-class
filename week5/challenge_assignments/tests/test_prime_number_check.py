import pytest
from prime_number_check import is_prime

def test_prime_number_check():
    assert is_prime(2) is True  # Smallest prime
    assert is_prime(3) is True  # Prime
    assert is_prime(4) is False  # Not prime
    assert is_prime(29) is True  # Prime
    assert is_prime(1) is False  # Not prime
    assert is_prime(0) is False  # Not prime
