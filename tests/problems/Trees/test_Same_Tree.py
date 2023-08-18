from ....problems.Trees.Same_Tree import create_Binary_Tree, Solution
from hypothesis.strategies import lists, integers, composite
from hypothesis import given
import pytest


@composite
def get_params(draw):
    size = draw(integers(min_value=0, max_value=50))
    TreeList1 = draw(lists(integers(), min_size=size, max_size=size))
    TreeList2 = draw(lists(integers(), min_size=size, max_size=size))
    expected = True if TreeList1 == TreeList2 else False

    return [TreeList1, TreeList2, expected]


t = Solution()


# Test using different methods = Recursion, DFS, BFS
@pytest.mark.parametrize(
    "TreeList1, TreeList2, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], False),
        ([2, 1, 3], [2, 1, 3], True),
        ([], [], True),
        ([3, 9, 20, None, None, 15, 7], [3, 9, 20, None, None, 15, 7], True),
        ([1, None, 2], [1, None, 2], True),
        ([1, 2, 3, 4, 5, None, None], [1, 2, 3, 4, 5, None, None], True),
        (
            [4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7],
            [4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7],
            True,
        ),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 2, 3, 3, None, None, 4, 4], [1, 2, 2, 3, 3, None, None, 4, 4], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_is_same_tree_parametrize(
    TreeList1: list, TreeList2: list, expected: list
) -> None:
    tree1 = create_Binary_Tree(TreeList1)
    tree2 = create_Binary_Tree(TreeList2)
    test = Solution()
    res = test.isSameTree(tree1, tree2)

    assert res == expected


@given(get_params())
def test_is_same_tree_startegies(params: list) -> None:
    expected = params.pop()
    TreeList2 = params.pop()
    TreeList1 = params.pop()

    tree1 = create_Binary_Tree(TreeList1)
    tree2 = create_Binary_Tree(TreeList2)
    test = Solution()
    res = test.isSameTree(tree1, tree2)

    assert res == expected
