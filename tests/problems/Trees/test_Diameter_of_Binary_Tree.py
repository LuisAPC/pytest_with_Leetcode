from ....problems.Trees.Diameter_of_Binary_Tree import create_Binary_Tree, Solution
import pytest


# Test using different methods = Recursion, DFS, BFS
@pytest.mark.parametrize(
    "TreeList, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], 4),
        ([2, 1, 3], 2),
        ([], 0),
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 1),
        ([1, 2, 3, 4, 5, None, None], 3),
        ([4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7], 6),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1, 2, 2, 3, 3, None, None, 4, 4], 4),
        ([1, 2, 3], 2),
        ([1, 2, 1], 2),
    ],
)
def test_diameter_of_binary_tree_parametrize(TreeList: list, expected: list) -> None:
    tree = create_Binary_Tree(TreeList)
    test = Solution()
    res = test.diameterOfBinaryTree(tree)

    assert res == expected
