from ....problems.Trees.Subtree_of_Another_Tree import create_Binary_Tree, Solution
import pytest


@pytest.mark.parametrize(
    "root, subRoot, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], False),
        ([2, 1, 3], [2, 1, 3], True),
        ([], [], False),
        ([3, 9, 20, None, None, 15, 7], [3, 9, 20, None, None, 15, 7], True),
        ([1, None, 2], [1, None, 2], True),
        ([1, 2, 3, 4, 5, None, None], [1, 2, 3, 4, 5, None, None], True),
        ([4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7], [1, 3, 4], True),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 2, 3, 3, None, None, 4, 4], [1, 2, 2, 3, 3, None, None], False),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 1], [1, 1, 2], False),
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
        ([1, 1], [1], True),
    ],
)
def test_is_same_tree_parametrize(root: list, subRoot: list, expected: list) -> None:
    tree1 = create_Binary_Tree(root)
    tree2 = create_Binary_Tree(subRoot)
    test = Solution()
    res = test.isSubtree(tree1, tree2)

    assert res == expected
