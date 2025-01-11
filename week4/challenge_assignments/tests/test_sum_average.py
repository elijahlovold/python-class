import pytest

from calculate_sum_and_average import eval_sum_and_average

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], (10, 2.5)),
        ([10, 20], (30, 15.0)),
    ]
)
def test_calculate_sum_and_average(nums, expected):
    assert eval_sum_and_average(nums) == expected
