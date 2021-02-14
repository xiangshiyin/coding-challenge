# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def helper(n, curr, output, l_counter, r_counter):
#             if l_counter==n and r_counter==n:
#                 output.append(''.join(curr))
#             if l_counter < n:
#                 curr.append('(')
#                 helper(n, curr, output, l_counter+1, r_counter)
#                 curr.pop()
#             if r_counter < l_counter:
#                 curr.append(')')
#                 helper(n, curr, output, l_counter, r_counter+1)
#                 curr.pop()
        
#         l_counter = 0
#         r_counter = 0
#         curr = []
#         output = []
#         helper(n, curr, output, l_counter, r_counter)
#         return output


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n, curr, output, l_counter, r_counter):
            if l_counter==n and r_counter==n:
                output.append(curr)
            if l_counter < n:
                helper(n, curr+'(', output, l_counter+1, r_counter)
            if r_counter < l_counter:
                helper(n, curr+')', output, l_counter, r_counter+1)
        
        l_counter = 0
        r_counter = 0
        curr = ''
        output = []
        helper(n, curr, output, l_counter, r_counter)
        return output

