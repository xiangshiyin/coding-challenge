#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         """
#         Time limit exceeded
#         """
#         n = len(s)
#         if n == 1:
#             return s
#         grid = [[0] * (n - i) for i in range(n)]
#         maxL = 1
#         l = 0
#         r = 0
#         for start in range(n)[::-1]:
#             for delta in range(n - start):
#                 if delta == 0:
#                     grid[start][delta] = 1
#                 elif delta == 1:
#                     grid[start][delta] = 1 if s[start] == s[start + delta] else 0
#                 else:
#                     grid[start][delta] = (
#                         1
#                         if s[start] == s[start + delta]
#                         and grid[start + 1][delta - 2] == 1
#                         else 0
#                     )
#                 if grid[start][delta] and delta + 1 >= maxL:
#                     maxL = delta + 1
#                     l = start
#                     r = start + delta

#         return s[l : r + 1]


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def palindrome(s, l, r):
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             return s[l + 1 : r]

#         maxL = 0
#         output = ""
#         for i in range(len(s)):
#             s1 = palindrome(s, i, i)
#             if len(s1) >= maxL:
#                 maxL = len(s1)
#                 output = s1
#             if i < len(s) - 1:
#                 s2 = palindrome(s, i, i + 1)
#                 if len(s2) >= maxL:
#                     maxL = len(s2)
#                     output = s2
#         return output


# solution on 2022-09-26
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        maxSubstring = ""
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            if len(s1) >= maxL:
                maxL = len(s1)
                maxSubstring = s1
            if i < len(s) - 1:
                s2 = self.palindrome(s, i, i + 1)
                if len(s2) >= maxL:
                    maxL = len(s2)
                    maxSubstring = s2
        return maxSubstring

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]


# @lc code=end
