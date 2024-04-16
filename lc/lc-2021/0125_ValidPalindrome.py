# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # remove the non-alphanumeric characters
#         s1 = [char.lower() for char in s if char.isalnum()]
#         return s1 == s1[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        
        if n == 1:
            return True
        
        l = 0
        r = n - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        return True
    
    