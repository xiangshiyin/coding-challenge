class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        i = 0
        n = len(s)

        while i <= n - k:
            if s[i : i + k] not in seen:
                seen.add(s[i : i + k])
            i += 1

        return len(seen) == 2**k
