class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # traverse the magazine, build a lookup table
        helper = {}
        for char in magazine:
            if char not in helper:
                helper[char] = 1
            else:
                helper[char] += 1

        # traverse the ransomNode
        for char in ransomNote:
            if char not in helper:
                return False
            elif helper[char] > 0:
                helper[char] -= 1
            else:
                return False
        return True
