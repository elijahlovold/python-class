import pytest 
from palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("racecar") is True  # Palindrome
    assert is_palindrome("level") is True  # Palindrome
    assert is_palindrome("hello") is False  # Not a palindrome
    assert is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()) is True  # Palindrome ignoring spaces/case
    assert is_palindrome("") is True  # Empty string
