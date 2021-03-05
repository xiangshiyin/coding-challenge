class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]:
                    return True
                else:
                    return False
        return True
                