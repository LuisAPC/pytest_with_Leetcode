from ....problems.Arrays_and_Hashing.Valid_Anagram import Solution
from hypothesis.strategies import from_regex, composite
from hypothesis import given
from collections import Counter
import pytest


@composite
def get_params(draw):
    s = draw(from_regex("^[a-z]+$", fullmatch=True))
    t = draw(from_regex("^[a-z]+$", fullmatch=True))
    expected = Counter(s) == Counter(t)

    return [s, t, expected]


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("red", "de", False),
        ("hi", "hello", False),
    ],
)
def test_is_anagram_parametrize(s: str, t: str, expected: bool) -> None:
    test = Solution()

    assert test.isAnagram(s, t) == expected


@given(get_params())
def test_is_anagram_strategies(params: list) -> None:
    s = params[0]
    t = params[1]
    expected = params[2]
    print(params)
    test = Solution()

    assert test.isAnagram(s, t) == expected
