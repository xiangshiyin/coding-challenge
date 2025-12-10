class Solution:
    def romanToInt(self, s: str) -> int:
        r2n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)

        # exception
        if n == 1:
            return r2n[s]

        # traverse the string
        result = 0
        i = 0

        while i < n - 1:  # leave the last digit alone
            while i < n - 1 and r2n[s[i]] >= r2n[s[i + 1]]:
                result += r2n[s[i]]
                i += 1
            if i < n - 1:
                result += r2n[s[i + 1]] - r2n[s[i]]
                i += 2

        if i < n:
            result += r2n[s[-1]]
        return result
