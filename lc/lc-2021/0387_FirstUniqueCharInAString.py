class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create a lookup table
        helper = {}
        for char in s:
            if char not in helper:
                helper[char] = 1
            else:
                helper[char] += 1
        print(helper)
        
        # 2nd pass
        for i in range(len(s)):
            if helper[s[i]]==1:
                return i
        return -1
        