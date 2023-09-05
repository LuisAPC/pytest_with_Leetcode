# import sys
# sys.path.append(r"C:\Users\luisp\Desktop\Leetcode\problems")
# from Linked_List_Cycle import create_linked_list, Solution, ListNode
from __future__ import annotations

from ....problems.Arrays_and_Hashing.Two_Sum import Solution
from typing import Optional
import pytest


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum_parametrize(nums: Optional[list], target: int, expected: bool) -> None:
    test = Solution()

    assert test.twoSum(nums, target) == expected
