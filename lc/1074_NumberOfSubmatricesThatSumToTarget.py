class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        '''
        compress the matrix
        '''
        m = len(matrix)
        n = len(matrix[0])
                    
        def helper(tmp, target):
            from collections import defaultdict
            presums = defaultdict(int)
            presums[0] += 1
            presum = 0
            num = 0
            for v in tmp:
                presum += v
                if presum - target in presums:
                    num += presums[presum - target]
                presums[presum] += 1
            
            return num
        
        counter = 0
        for i in range(m):
            tmp = [0] * n
            for j in range(i, m):
                for k in range(n):
                    tmp[k] += matrix[j][k]
                # for each combination, check the number of subarrays sum to target
                delta = helper(tmp, target)
                counter += delta
                # print(tmp, counter, delta)
            
        return counter        
                
                