from ....problems.Sliding_Window.Best_Time_to_Buy_and_Sell_Stock import Solution
import pytest


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_two_sum_parametrize(prices: list, expected: int) -> None:
    test = Solution()

    assert test.maxProfit(prices) == expected
