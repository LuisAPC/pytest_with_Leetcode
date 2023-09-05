from ....problems.Binary_Search.Binary_Search import Solution
from hypothesis.strategies import lists, integers, composite
from hypothesis import given
import pytest


@composite
def get_params(draw):
    size = draw(integers(min_value=1, max_value=100))
    nums = draw(lists(integers(), min_size=size, max_size=size, unique=True,))
    nums.sort()
    target = draw(integers())
    expected = nums.index(target) if target in set(nums) else -1

    return [nums, target, expected]


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_search_parametrize(nums: list, target: int, expected: int) -> None:
    test = Solution()

    assert test.search(nums, target) == expected


@given(get_params())
def test_search_strategies(params: list) -> None:
    print(params)
    expected = params[2]
    target = params[1]
    nums = params[0]

    test = Solution()

    assert test.search(nums, target) == expected
