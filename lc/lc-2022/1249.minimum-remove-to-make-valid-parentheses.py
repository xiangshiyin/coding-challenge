#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        # mark invalid )
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""

        # mark invalid (
        while stack:
            s[stack.pop()] = ""

        return "".join(s)


# @lc code=end
