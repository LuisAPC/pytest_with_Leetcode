# import sys
# sys.path.append(r"C:\Users\luisp\Desktop\Leetcode\problems")
# from Linked_List_Cycle import create_linked_list, Solution, ListNode

from ...problems.Linked_List_Cycle import create_linked_list, Solution, ListNode
from hypothesis.strategies import lists, integers, booleans, composite, SearchStrategy
from hypothesis import given
from typing import Optional, Callable
import pytest


@composite
def get_params(draw):
    size = draw(integers(min_value=0, max_value=100))
    LinkedList = draw(lists(integers(), min_size=size, max_size=size))
    cycle_to_node = draw(integers(min_value=-1, max_value=size - 1))
    expected = True if cycle_to_node > -1 else False

    return [LinkedList, cycle_to_node, expected]


@pytest.mark.parametrize(
    "LinkedList, cycle_to_node, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1], 0, True),
        ([], -1, False),
    ],
)
def test_has_cycle_parametrize(
    LinkedList: Optional[list], cycle_to_node: int, expected: bool
) -> None:
    head = create_linked_list(LinkedList, cycle_to_node)
    test = Solution()

    assert test.hasCycle(head) == expected


@given(get_params())
def test_has_cycle_strategies(params: list) -> None:
    print(params)
    expected = params.pop()
    cycle_to_node = params.pop()
    LinkedList = params.pop()

    head = create_linked_list(LinkedList, cycle_to_node)
    test = Solution()

    assert test.hasCycle(head) == expected
