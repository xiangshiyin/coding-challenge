# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         ans = ''
#         for char in s:
#             ans += char
#             if len(ans) >= k and ans[-k:] == ans[-1] * k:
#                 ans = ans[:-k] 
#         return ans
            
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        stack, save the char and frequency
        '''
        stack = []
        for char in s:
            if len(stack) == 0 or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        return ''.join([v[0] * v[1] for v in stack])
        