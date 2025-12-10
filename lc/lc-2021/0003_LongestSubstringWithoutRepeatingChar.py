# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:58:47 2017

@author: xyin
"""

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         visited = {}
#         maxlength = 0
#         low = 0
#         high = -1
#         for index, letter in enumerate(s):
#             if visited.get(letter, None) is not None:
#                 visited[letter].append(index)
#                 if low <= visited[letter][-2]:
#                     low = visited[letter][-2] + 1
#             else:
#                 visited[letter] = [index]
#             high += 1
#             length = high - low + 1
#             if length > maxlength:
#                 maxlength = length
#             # print(visited[letter], low, high)
#         return(maxlength)

# on 1/4/2021
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # exceptions
#         if s=='':
#             return 0
#         # traverse the string, label the ones visited
#         start = 0
#         end = 0
#         max_len = 0
#         tb = {}
#         while end < len(s):
#             if s[end] in tb:
#                 # update the start pointer
#                 max_len = max(max_len, end-start)
#                 start = tb[s[end]]+1
#             # update the lookup table
#             tb[s[end]] = end
#             # update the pointer
#             end += 1
#         # if no repeated character showed up
#         max_len = max(max_len, end-start)
#         return max_len

# on 2/5/2021
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         N = len(s)
#         # exceptions
#         if N <= 1:
#             return N

#         # traverse string, utilize hash table to help check repeated chars
#         tb = {}
#         start = 0
#         end = 0
#         max_len = 0
#         while end < N and end >= start:
#             if s[end] in tb and tb[s[end]] >= start:
#                 max_len = max(max_len, end - start)
#                 start = tb[s[end]] + 1

#             tb[s[end]] = end
#             end += 1

#         max_len = max(max_len, end - start)

#         return max_len


# as of 11/13/2021
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        maxL = 0
        n = len(s)
        if n <= 1:
            return n

        l = r = 0
        while r < n:
            if s[r] not in lookup:
                lookup.add(s[r])
            else:
                maxL = max(maxL, r - l)
                while s[l] != s[r]:
                    lookup.remove(s[l])
                    l += 1
                l += 1
            r += 1
        maxL = max(maxL, r - l)
        return maxL


# # solution as of 11/28/2021
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         '''
#         use hash map to save index of all visited chars
#         '''
#         n = len(s)
#         maxLen = 0
#         l = 0
#         visited = {}

#         for r in range(n):
#             if s[r] in visited:
#                 l = max(l, visited[s[r]]+1)
#             maxLen = max(maxLen, r-l+1)
#             visited[s[r]] = r

#         return maxLen


# solution as of 8/24/2022
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start = 0
        maxL = 0
        lookup = {}

        for i, v in enumerate(s):
            if v in lookup and lookup[v] >= start:
                start = lookup[v] + 1
            lookup[v] = i
            maxL = max(maxL, i - start + 1)

        return maxL
