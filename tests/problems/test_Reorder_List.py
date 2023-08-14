import sys

sys.path.append(r"C:\Users\luisp\Desktop\Leetcode\problems")
from Reorder_List import create_linked_list, Solution

# from ...problems.Reorder_List import create_linked_list, Solution
from hypothesis.strategies import lists, integers, tuples
from hypothesis import given
from typing import Optional
import pytest


def merge_lists(list1: Optional[list], list2: Optional[list]) -> list:
    l1 = create_linked_list(list1)
    l2 = create_linked_list(list2)

    test = Solution()
    res = test.mergeTwoLists(l1, l2)
    res = list(res) if res else []

    return res


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_lists_parametrize(
    list1: Optional[list], list2: Optional[list], expected: Optional[list]
) -> None:
    res = merge_lists(list1, list2)

    assert res == expected


@given(lists(integers()).map(sorted), lists(integers()).map(sorted))
def test_merge_lists_strategies(list1: Optional[list], list2: Optional[list]) -> None:
    res1 = merge_lists(list1, list2)
    res2 = merge_lists(list2, list1)

    same_len = len(res1) == (len(list1)+len(list2))

    assert res1 == res2 and same_len
