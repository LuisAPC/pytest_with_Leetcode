class Solution:
    def maxProfit(self, prices: list) -> int:
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            if sell < buy:
                buy = sell

            cur_profit = sell - buy
            max_profit = max(max_profit, cur_profit)
        return max_profit


test = Solution()
print(test.maxProfit([7, 1, 5, 3, 6, 4]))
