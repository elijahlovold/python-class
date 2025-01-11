import pytest

from check_sorted import eval_is_sorted

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5], True),  # Already sorted
        ([5, 4, 3, 2, 1], False),  # Descending order
        ([1, 2, 2, 3], True),      # Contains duplicates
        ([1], True),               # Single element
        ([], True),                # Empty list
        ([3, 2, 4], False),        # Unsorted
    ]
)
def test_is_sorted(lst, expected):
    assert eval_is_sorted(lst) == expected
