class Solution:
    def countSubstrings(self, s: str) -> int:
        self.counter = 0
        
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                self.counter += 1
        
        for i in range(len(s)):
            
            # check the palindromic strings centered at i
            helper(s, i, i)
            
            # check the palindromic strings centered at (i, i + 1)
            helper(s, i, i + 1)
        
        return self.counter
            