# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         n = len(pushed)
#         # exception
#         if n == 0:
#             return True
        
#         # create a hash table of value-index pairs
#         tb = {v:i for i,v in enumerate(pushed)}
#         visited = set()
        
#         # traverse popped
#         i = 0
#         while i < n:
#             if i == 0:
#                 stack = [j for j in range(tb[popped[i]])]
#                 # print(stack)
#             else:
#                 if tb[popped[i]] > tb[popped[i - 1]]:
#                     if len(stack) > 0:
#                         for j in range(stack[-1] + 1, tb[popped[i]]):
#                             if j not in visited:
#                                 stack.append(j)
#                     else:
#                         for j in range(tb[popped[i - 1]] + 1, tb[popped[i]]):
#                             if j not in visited:
#                                 stack.append(j)
#                 else:
#                     if tb[popped[i]] != stack[-1]:
#                         return False
#                     else:
#                         stack.pop()
#                 # print(stack)
#             visited.add(tb[popped[i]])
#             i += 1
        
#         return True
                

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # exception
        if len(pushed) == 0:
            return True
        
        stack = []
        i = 0
        for v in pushed:
            stack.append(v)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return len(stack) == 0
    
    