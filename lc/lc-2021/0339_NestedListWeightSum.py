# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# class Solution:
#     def depthSum(self, nestedList: List[NestedInteger]) -> int:
#         '''
#         The BFS solution
#         '''
#         from collections import deque
#         total = 0
        
#         # initialize the queue
#         queue = deque([[1, item] for item in nestedList])
        
#         # bfs search and update total
#         while queue:
#             # pop left
#             level, item = queue.popleft()
#             # evaluate
#             if item.isInteger():
#                 total += level * item.getInteger()
#             else:
#                 # append the children
#                 for element in item.getList():
#                     queue.append([level+1, element])
#         return total
            
            
# class Solution:
#     def depthSum(self, nestedList: List[NestedInteger]) -> int:
#         '''
#         The DFS solution
#         '''
#         total = 0
        
#         # dfs search and update total
#         for element in nestedList:
#             # get an element
#             level = 1
            
#             def traverse(item, level, total):
#                 if item.isInteger():
#                     total += level * item.getInteger()
#                     return total
#                 else:
#                     for subitem in item.getList():
#                         total += traverse(subitem, level+1, 0)
#                 return total
#             total += traverse(element, level, 0)
#         return total
            
                
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        '''
        The DFS solution with stack
        '''
        total = 0
        
        # dfs search and update total
        for element in nestedList:
            stack = [[1,element]]
            while stack:
                # pop
                level,item = stack.pop()
                # evaluate
                if item.isInteger():
                    total += level*item.getInteger()
                else:
                    # append children
                    for subitem in item.getList():
                        stack.append([level+1, subitem])
                        
        return total 
    
