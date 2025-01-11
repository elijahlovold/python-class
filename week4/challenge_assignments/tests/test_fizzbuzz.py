import pytest

from fizzbuzz import eval_fizzbuzz

@pytest.mark.parametrize(
    "n, expected",
    [
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (7, "7"),
    ]
)
def test_eval_fizzbuzz(n, expected):
    assert eval_fizzbuzz(n) == expected
    
