from ....problems.Stack.Valid_Parentheses import Solution
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("()[", False)
    ]
)
def test_is_valid_parametrize(s: str, expected: bool) -> None:
    test = Solution()

    assert test.isValid(s) == expected
