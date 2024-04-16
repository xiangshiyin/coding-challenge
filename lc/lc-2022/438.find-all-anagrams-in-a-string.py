#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         from collections import Counter, defaultdict

#         pattern = Counter(p)
#         ans = []
#         found = defaultdict(int)
#         start = -1
#         for i in range(len(s)):
#             if s[i] in pattern:
#                 if start == -1:
#                     start = i

#                 found[s[i]] += 1
#                 if i - start + 1 == len(p):
#                     if found == pattern:
#                         ans.append(start)
#                     found[s[start]] -= 1
#                     start += 1
#             else:
#                 if found:
#                     if found == pattern:
#                         ans.append(start)
#                     else:
#                         found = defaultdict(int)
#                     start = -1
#         return ans


# solution on 2022-09-19
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict, Counter

        freq = Counter(p)
        sofar = defaultdict(int)
        n = len(s)
        l = 0
        r = 0
        ans = []
        while l <= r and r < n:
            if s[r] not in freq:
                r += 1
                l = r
            else:
                if l == r:
                    sofar = defaultdict(int)
                sofar[s[r]] += 1

                while r - l + 1 > len(p):
                    sofar[s[l]] -= 1
                    l += 1

                if r - l + 1 == len(p):
                    if sofar == freq:
                        ans.append(l)
                    else:
                        sofar[s[l]] -= 1
                        l += 1
                r += 1
        return ans


# @lc code=end

