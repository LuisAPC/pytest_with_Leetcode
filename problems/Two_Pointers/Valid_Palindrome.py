class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # with built-in methods
        # chars_only = ''
        # for c in s:
        #     if c.isalnum():
        #         chars_only += c.lower()

        # return chars_only == chars_only[::-1]

        # whithout built-in mehtods
        def check_alnum(c: str) -> bool:
            return (
                ord("a") <= ord(c) <= ord("z")
                or ord("A") <= ord(c) <= ord("Z")
                or ord("0") <= ord(c) <= ord("9")
            )

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not check_alnum(s[l]):
                l += 1

            while l < r and not check_alnum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))
