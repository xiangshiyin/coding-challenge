# class Solution:
#     def lengthLongestPath(self, input: str) -> int:
#         '''
#         1. use stack to traverse the tree
#         2. use *.xxx to identify the leaves
#         '''
#         input2 = input.split('\n')
#         stack = []
#         len_cur = 0
#         len_max = 0
#         # print(input2)
        
#         for ipt in input2:
#             # find the tabs
#             ix = 0
#             while ix < len(ipt) and ipt[ix] == '\t':
#                 ix += 1
            
#             # evaluate the current path
#             if '.' not in ipt[ix:]: # a directory
#                 # update the stack
#                 while stack and stack[-1][0] >= ix:
#                     len_cur -= stack[-1][1]
#                     stack.pop()
#                 len_cur_tmp = len(ipt) - ix if len_cur == 0 else len(ipt) - ix + 1
#                 # push
#                 stack.append((ix, len_cur_tmp))
#                 len_cur += len_cur_tmp
                    
#             else: # a file
#                 # update the stack
#                 while stack and stack[-1][0] >= ix:
#                     len_cur -= stack[-1][1]
#                     stack.pop()
                
#                 len_max = max(len_max, len_cur + len(ipt) - ix) if len_cur == 0 else max(len_max, len_cur + len(ipt) - ix + 1)
            
#         return len_max

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        '''
        others' solution
        '''
        input2 = input.split('\n')
        len_max = 0
        len_path = {0:0}
        for ipt in input2:
            name = ipt.lstrip('\t')
            depth = len(ipt) - len(name)
            if '.' in name:
                len_max = max(len_max, len_path[depth] + len(name))
            else:
                len_path[depth + 1] = len_path[depth] + 1 + len(name)
        print(depth, len_path)
        
        return len_max
    
        