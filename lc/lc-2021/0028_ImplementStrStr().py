class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # special case
        if needle == "":
            return 0

        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1

        ix = 0
        while ix < m - n + 1:
            if haystack[ix] == needle[0]:
                if haystack[ix : ix + n] == needle:
                    return ix
            ix += 1
        return -1
