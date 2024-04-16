#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter

        pattern = Counter(secret)
        n = len(secret)
        bulls = 0
        cows = 0

        for i in range(n):
            if guess[i] == secret[i]:
                bulls += 1
                pattern[guess[i]] -= 1
        for i in range(n):
            if guess[i] != secret[i] and guess[i] in pattern and pattern[guess[i]] > 0:
                cows += 1
                pattern[guess[i]] -= 1
        return f"{bulls}A{cows}B"


# @lc code=end

