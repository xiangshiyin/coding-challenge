#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter, defaultdict

        pattern = Counter(p)
        ans = []
        found = defaultdict(int)
        start = -1
        for i in range(len(s)):
            if s[i] in pattern:
                if start == -1:
                    start = i

                found[s[i]] += 1
                if i - start + 1 == len(p):
                    if found == pattern:
                        ans.append(start)
                    found[s[start]] -= 1
                    start += 1
            else:
                if found:
                    if found == pattern:
                        ans.append(start)
                    else:
                        found = defaultdict(int)
                    start = -1
        return ans


# @lc code=end

