class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        # exception
        if N<=1:
            return 0
        
        # traverse the string from right to left
        longest = 0
        lcounter = 0
        rcounter = 0
        marker = 0
        
        for i,char in enumerate(s):
            if char=='(':
                lcounter += 1
            else:
                rcounter += 1
            if rcounter > lcounter:
                longest = max(lcounter*2, longest)
                lcounter = 0 # clear ( counter
                rcounter = 0 # clear ) counter
                marker = i+1
        
        if lcounter==rcounter:
            longest = max(lcounter*2, longest)
        else:
            # traverse the section where redundant "(" might exist from right to left
            lcounter = 0
            rcounter = 0
            for j in range(N-1,marker-1,-1):
                if s[j]=='(':
                    lcounter += 1
                else:
                    rcounter += 1
                # print(lcounter, rcounter)
                if rcounter < lcounter:
                    longest = max(rcounter*2, longest)
                    lcounter = 0
                    rcounter = 0
            longest = max(rcounter*2, longest)
            
        
        return longest
                    
                
        