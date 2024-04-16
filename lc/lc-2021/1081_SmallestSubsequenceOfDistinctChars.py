class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # create frequence table
        from collections import Counter
        tb = Counter(s)
        
        # create table to check existence
        exist = {char:0 for char in set(s)}
        
        # traverse the string
        stack = []
        
        for char in s:
            if exist[char] == 0:
                while stack and char <= stack[-1] and tb[stack[-1]] >= 1:
                    exist[stack[-1]] = 0
                    stack.pop()
                    
                stack.append(char)
                exist[char] = 1
                tb[char] -= 1
            else:
                tb[char] -= 1
            # print(stack)
        
        return ''.join(stack)
            