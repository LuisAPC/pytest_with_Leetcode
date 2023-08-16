from ...problems.Maximum_Depth_of_Binary_Tree import create_Binary_Tree, Solution
import pytest


# Test using different methods = Recursion, DFS, BFS
@pytest.mark.parametrize(
    "TreeList, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], 3),
        ([2, 1, 3], 2),
        ([], 0),
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([1, 2, 3, 4, 5, None, None], 3),
        ([4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7], 4),
    ],
)
def test_max_Depth_parametrize(TreeList: list, expected: list) -> None:
    tree = create_Binary_Tree(TreeList)
    test = Solution()
    recursion_res = test.recursionMaxDepth(tree)
    BFS_res = test.BFSMaxDepth(tree)
    DFS_res = test.DFSMaxDepth(tree)

    assert recursion_res == BFS_res == DFS_res == expected
