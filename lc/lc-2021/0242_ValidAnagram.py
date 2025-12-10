class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # record the character frequencies
        tbs = {}
        for char in s:
            if char not in tbs:
                tbs[char] = 1
            else:
                tbs[char] += 1

        # traverse string t
        for char in t:
            if char in tbs and tbs[char] > 0:
                tbs[char] -= 1
            else:
                return False
        return True
