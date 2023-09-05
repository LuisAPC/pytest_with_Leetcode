class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # ONE LINE SOL
        # return len(set(nums)) != len(nums)

        # NORMAL SOL
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


test = Solution()
print(test.containsDuplicate([1, 2, 3, 1]))
