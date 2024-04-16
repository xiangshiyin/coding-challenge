#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter

        wordcount = Counter(words)
        # traverse the word pool
        seen = set()
        ans = 0
        singleton = 0
        for w in wordcount.keys():
            w2 = w[::-1]
            if w not in seen and w2 not in seen:
                if w2 in wordcount:
                    if w2 != w:
                        ans += 2 * 2 * min(wordcount[w], wordcount[w2])
                    else:
                        ans += 2 * 2 * (wordcount[w] // 2)
                        if singleton == 0 and wordcount[w] % 2 == 1:
                            singleton = 2
                seen.add(w)
                seen.add(w2)
        return ans + singleton


# @lc code=end
