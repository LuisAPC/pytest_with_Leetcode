from ...problems.Reverse_Linked_List import Solution, create_linked_list
from hypothesis import given
from hypothesis.strategies import lists, integers
import pytest


@pytest.mark.parametrize(
    "input_list, reversed_list",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([0], [0]),
        ([None], [None]),
        ([-5000, 0, 5000], [5000, 0, -5000]),
    ],
)
def test_reversed_linked_list_parametrize(input_list, reversed_list):
    head = create_linked_list(input_list)

    test = Solution()
    res = test.reverseList(head)

    assert list(res) == reversed_list


@given(lists(integers(), min_size=1))
def test_reverse_linked_list_strategies(ls):
    head = create_linked_list(ls)

    test = Solution()
    res = list(test.reverseList(head))
    res.reverse()

    assert res == ls


def test_no_linked_list():
    head = create_linked_list([None])

    test = Solution()
    res = list(test.reverseList(head))
    res.reverse()

    assert res == [None]
