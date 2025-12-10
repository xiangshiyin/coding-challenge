class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        pool = set("aeiouAEIOU")

        # two pointers starting from the middle
        l = n // 2 - 1
        r = n // 2
        lcounter = 0
        rcounter = 0

        while l >= 0 and r < n:
            if s[l] in pool:
                lcounter += 1
            if s[r] in pool:
                rcounter += 1
            l -= 1
            r += 1

        return lcounter == rcounter
