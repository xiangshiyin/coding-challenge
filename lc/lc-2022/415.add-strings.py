#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carryover = 0
        ans = ""
        while p1 >= 0 and p2 >= 0:
            currDigit = (int(num1[p1]) + int(num2[p2]) + carryover) % 10
            carryover = (int(num1[p1]) + int(num2[p2]) + carryover) // 10
            ans = f"{currDigit}" + ans
            p1 -= 1
            p2 -= 1

        p = p1 if p1 >= 0 else p2
        num = num1 if p1 >= 0 else num2
        while p >= 0:
            currDigit = (int(num[p]) + carryover) % 10
            carryover = (int(num[p]) + carryover) // 10
            ans = f"{currDigit}" + ans
            p -= 1
        if carryover:
            ans = f"{carryover}" + ans
        # trim leading 0
        i = 0
        while i < len(ans) - 1 and ans[i] == "0":
            i += 1
        return ans


# @lc code=end
