#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         # track letter frequencies
#         from collections import Counter
#         freqs = Counter(s)
#         # find all the even pairs and odd center
#         maxL = 0
#         for l,f in freqs.items():
#             maxL += (f // 2) * 2
#             if maxL % 2 == 0 and f % 2 == 1:
#                 maxL += 1
#         return maxL


# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         from collections import Counter

#         freq = Counter(s)
#         maxL = 0
#         for f in freq.values():
#             maxL += (f // 2) * 2
#             if maxL % 2 == 0 and f % 2 == 1:
#                 maxL += 1
#         return maxL


# solution on 2022-09-26
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        length = 0
        for f in freq.values():
            length += 2 * (f // 2)
            if length % 2 == 0 and f % 2 == 1:
                length += 1
        return length


# @lc code=end
