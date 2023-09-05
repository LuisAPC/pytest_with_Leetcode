# from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        s_dict = {}  # char : ocurrences
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        for key, val in s_dict.items():
            if t_dict.get(key, 0) != val:
                return False
        return True

        # # SAME AS ABOVE BUT USING COLLECTIONS LIBRARY (COUNTER)
        # return Counter(t) == Counter(s)

        # # SORTING ALSO WORKS BUT O(NLOGN) INSTEAD OF ABOVE O(N)
        # return sorted(t) == sorted(s)


test = Solution()
print(test.isAnagram(s="anagram", t="nagaram"))
