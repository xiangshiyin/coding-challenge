class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # build a hash map
        helper = {}
        counter_odd = 0
        # traverse the string
        for l in s:
            if l in helper:
                helper[l] += 1
                if helper[l]%2==0:
                    counter_odd -= 1
                else:
                    counter_odd += 1
            else:
                helper[l] = 1
                counter_odd += 1
        if counter_odd<=1:
            return True
        else:
            return False
        
        