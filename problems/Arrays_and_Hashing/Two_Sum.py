from __future__ import annotations


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsMap = {}  # val : idx

        for i, n in enumerate(nums):
            diff = target - n

            if diff in numsMap:
                return [numsMap[diff], i]

            numsMap[n] = i


test = Solution()
print(test.twoSum(nums=[2, 7, 11, 15], target=9))
