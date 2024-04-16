class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for char in num:
            while stack and int(char) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(char)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        if stack:
            return str(int(''.join(stack)))
        else:
            return '0'
        
        