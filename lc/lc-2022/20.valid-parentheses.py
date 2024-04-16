#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for v in s:
            if v in left:
                stack.append(v)
            else:
                if not stack:
                    return False
                elif v == left[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


# @lc code=end

