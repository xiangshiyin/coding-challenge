#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                tmp = ""
                while stack and stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()  # pop "["
                k = ""
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack.append(tmp * int(k))
        return "".join(stack)


# @lc code=end

