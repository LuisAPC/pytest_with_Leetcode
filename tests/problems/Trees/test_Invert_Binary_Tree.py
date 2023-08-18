from ....problems.Trees.Invert_Binary_Tree import create_Binary_Tree, Solution
import pytest

test = Solution()


@pytest.mark.parametrize(
    "TreeList, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        (
            list(test.invertTree(create_Binary_Tree([3, 9, 20, None, None, 15, 7]))),
            [3, 9, 20, None, None, 15, 7],
        ),
        ([1, None, 2], [1, 2, None]),
        (
            list(test.invertTree(create_Binary_Tree([1, 2, 3, 4, 5, None, None]))),
            [1, 2, 3, 4, 5, None, None],
        ),
        (
            list(
                test.invertTree(
                    create_Binary_Tree([4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7])
                )
            ),
            [4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7],
        ),
    ],
)
def test_invert_tree_parametrize(TreeList: list, expected: list) -> None:
    tree = create_Binary_Tree(TreeList)
    test = Solution()
    res = test.invertTree(tree)
    res = list(res) if res else []

    assert res == expected
