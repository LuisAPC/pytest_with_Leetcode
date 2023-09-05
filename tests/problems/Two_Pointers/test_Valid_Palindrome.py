from ....problems.Two_Pointers.Valid_Palindrome import Solution
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]
)
def test_is_palindrome_parametrize(s: str, expected: bool) -> bool:
    test = Solution()

    assert test.isPalindrome(s) == expected
