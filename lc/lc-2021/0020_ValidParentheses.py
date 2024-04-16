class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        
        helper = {
            '(':1,
            '[':2,
            '{':3,
            ')':-1,
            ']':-2,
            '}':-3
        }
        
        stack = []
        
        for char in s:
            if len(stack)==0:
                stack.append(char)
            elif helper[char]+helper[stack[-1]]==0 and helper[char]<helper[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)
        if len(stack)>0:
            return False
        else:
            return True
                
        
            