class Solution:
    def search(self, nums: list, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1


test = Solution()
print(test.search(nums=[0, -1, 1], target=0))
