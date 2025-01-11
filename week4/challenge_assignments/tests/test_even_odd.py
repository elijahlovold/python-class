import pytest

from even_odd import eval_even_odd

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], ["odd", "even", "odd", "even"]),
        ([0, 5, 10], ["even", "odd", "even"]),
    ]
)
def test_check_even_odd(nums, expected):
    assert eval_even_odd(nums) == expected
