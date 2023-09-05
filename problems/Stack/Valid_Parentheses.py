class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in char_dict:
                stack.append(char_dict[c])
            else:
                if not stack or stack.pop() != c:
                    return False

        return not stack


test = Solution()
print(test.isValid("()[]{}"))
