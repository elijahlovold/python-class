import pytest
from remove_duplicates import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]  # Remove duplicates
    assert remove_duplicates([4, 5, 4, 4, 6, 5]) == [4, 5, 6]  # Remove duplicates
    assert remove_duplicates([]) == []  # Empty list
    assert remove_duplicates([1, 1, 1, 1]) == [1]  # Single unique element
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]  # No duplicates
