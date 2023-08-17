from ...problems.Balanced_Binary_Tree import create_Binary_Tree, Solution
import pytest


# Test using different methods = Recursion, DFS, BFS
@pytest.mark.parametrize(
    "TreeList, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], True),
        ([2, 1, 3], True),
        ([], True),
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, None, 2], True),
        ([1, 2, 3, 4, 5, None, None], True),
        ([4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7], False),
        ([1, 2, 3, 4, 5], True),
        ([1, 2], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([1, 2, 3], True),
        ([1, 2, 1], True),
    ],
)
def test_is_balanced_parametrize(TreeList: list, expected: list) -> None:
    tree = create_Binary_Tree(TreeList)
    test = Solution()
    res = test.isBalanced(tree)

    assert res == expected
