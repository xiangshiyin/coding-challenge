#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         """stack"""

#         def clean(string):
#             stack = []
#             for ch in string:
#                 if ch != "#":
#                     stack.append(ch)
#                 else:
#                     if stack:
#                         stack.pop()
#             return "".join(stack)

#         return clean(s) == clean(t)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        back1 = 0
        back2 = 0
        while True:
            while p1 >= 0 and (back1 or s[p1] == "#"):
                if s[p1] == "#":
                    back1 += 1
                else:
                    back1 -= 1
                p1 -= 1
            while p2 >= 0 and (back2 or t[p2] == "#"):
                if t[p2] == "#":
                    back2 += 1
                else:
                    back2 -= 1
                p2 -= 1
            if not (p1 >= 0 and p2 >= 0 and s[p1] == t[p2]):
                return p1 == p2 == -1

            p1 -= 1
            p2 -= 1


# @lc code=end
