# class Solution:
#     def decodeString(self, s: str) -> str:
#         pool = set('0123456789')
#         stack = []
#         for char in s:
#             if char != ']':
#                 stack.append(char)
#             else:
#                 chars = ''
#                 while stack[-1] != '[':
#                     chars = stack.pop() + chars
#                 stack.pop() # pop out '['
                
#                 reps = ''
#                 while stack and stack[-1] in pool:
#                     reps = stack.pop() + reps
                
#                 if reps == '':
#                     stack.append(chars)
#                 else:
#                     stack.append(chars * int(reps))

#         return ''.join(stack)
                
        
class Solution:
    def decodeString(self, s: str) -> str:
        '''
        replace the stack with a string
        '''
        pool = set('0123456789')
        stack = ''
        for char in s:
            if char != ']':
                stack += char
            else:
                chars = ''
                while stack[-1] != '[':
                    chars = stack[-1] + chars
                    stack = stack[:-1]
                stack = stack[:-1] # pop out '['
                
                reps = ''
                while stack and stack[-1] in pool:
                    reps = stack[-1] + reps
                    stack = stack[:-1]
                
                if reps == '':
                    stack += chars
                else:
                    stack += (chars * int(reps))

        return stack
    