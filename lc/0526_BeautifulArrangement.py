# class Solution:
#     def countArrangement(self, n: int) -> int:
#         visited = [0]*n
#         self.counter = 0
        
#         def helper(idx, n, visited):
#             if idx>n:
#                 self.counter += 1
#             for num in range(1,n+1):
#                 if visited[num-1]==0 and (num%idx==0 or idx%num==0):
#                     visited[num-1]=1
#                     helper(idx+1, n, visited)
#                     visited[num-1]=0
#         helper(1,n,visited)
        
#         return self.counter
                
class Solution:
    def countArrangement(self, n: int) -> int:
        '''
        bitmask solution from youtube, not so fast
        '''
        bitmask = 0
        self.counter = 0
        
        def helper(idx, n, bitmask):
            if idx==n+1:
                self.counter += 1
            for num in range(1,n+1):
                if (bitmask&(1<<(num-1)))==0 and (num%idx==0 or idx%num==0):
                    helper(idx+1, n, bitmask^(1<<(num-1)))
        helper(1,n,bitmask)
        
        return self.counter            
        