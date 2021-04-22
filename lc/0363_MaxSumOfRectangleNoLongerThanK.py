class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        from bisect import insort, bisect_left
        self.maxsum = -1 * 10 ** 6
        
        def helper(tmp, k):
            presum = 0
            presums = [0]
            for i in range(len(tmp)):
                presum += tmp[i]
                idx = bisect_left(presums, presum - k)
                if idx < len(presums):
                    self.maxsum = max(self.maxsum, presum - presums[idx])
                insort(presums, presum)

                
        
        
        for ix in range(m):
            tmp = [0] * n
            for jx in range(ix,m):
                for kx in range(n):
                    tmp[kx] += matrix[jx][kx]
                helper(tmp, k)
        
        return self.maxsum
        
        
        