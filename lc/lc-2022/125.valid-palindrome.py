#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = [c.lower() for c in s if c.isalnum()]
        print(s_cleaned)
        return s_cleaned == s_cleaned[::-1]


# @lc code=end
