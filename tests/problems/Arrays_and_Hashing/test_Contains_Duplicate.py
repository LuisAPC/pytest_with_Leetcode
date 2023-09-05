# import sys
# sys.path.append(r"C:\Users\luisp\Desktop\Leetcode\problems")
# from Linked_List_Cycle import create_linked_list, Solution, ListNode
from __future__ import annotations

from ....problems.Arrays_and_Hashing.Contains_Duplicate import Solution
from hypothesis.strategies import lists, integers, composite
from hypothesis import given
from typing import Optional
import pytest


@composite
def get_params(draw):
    size = draw(integers(min_value=0, max_value=100))
    list1 = draw(lists(integers(), min_size=size, max_size=size))
    expected = True if len(set(list1)) != len(list1) else False

    return [list1, expected]


@pytest.mark.parametrize(
    "list1, expected",
    [
        ([3, 2, 0, -4], False),
        ([1, 2], False),
        ([1], False),
        ([1, 1], True),
        ([], False),
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate_parametrize(list1: Optional[list], expected: bool) -> None:
    test = Solution()

    assert test.containsDuplicate(list1) == expected


@given(get_params())
def test_contains_duplicate_strategies(params: list) -> None:
    expected = params[1]
    list1 = params[0]
    test = Solution()

    assert test.containsDuplicate(list1) == expected
