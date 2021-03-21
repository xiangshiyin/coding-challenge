# class Solution:
#     def numFactoredBinaryTrees(self, arr: List[int]) -> int:
#         '''
#         dp, not so fast
        
#         dp[parent] = dp[leftchild] * dp[rightchild] + 1 (+1 when no children added)
#         '''
#         # sort the input in place
#         arr.sort()
#         # generate hashset for lookup
#         tb = set(arr)
#         n = len(arr)
        
#         # dp iterations
#         dp = {}
#         for i in range(n):
#             dp[arr[i]] = sum([
#                 dp[arr[j]] * dp[arr[i]/arr[j]] if arr[i]/arr[j] in tb else 0
#                 for j in range(i)
#             ]) + 1
        
#         # print(dp)
        
#         return sum([v for i,v in dp.items()]) % (10 ** 9 + 7)


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        '''
        dp, not so fast
        
        dp[parent] = dp[leftchild] * dp[rightchild] + 1 (+1 when no children added)
        '''
        # sort the input in place
        arr.sort()
        n = len(arr)
        
        # dp iterations
        dp = {}
        for parent in arr:
            dp[parent] = sum([
                dp[left] * dp.get(parent/left, 0) 
                for left in dp if parent % left == 0
            ]) + 1
        
        return sum(dp.values()) % (10 ** 9 + 7)

        

        