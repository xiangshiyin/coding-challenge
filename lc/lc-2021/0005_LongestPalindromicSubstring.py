class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        O(n2) solution
        """

        def getLength(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        max_len = 0
        start = 0
        for i in range(len(s)):
            curr_len = max(getLength(s, i, i), getLength(s, i, i + 1))
            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2
        return s[start : start + max_len]
