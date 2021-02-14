class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        N = len(A)
        # create hash table to record C+D combinations:
        cd = {}
        for i in range(N):
            for j in range(N):
                if C[i] + D[j] not in cd:
                    cd[C[i] + D[j]] = 1
                else:
                    cd[C[i] + D[j]] += 1
                    
        res = 0
        # loop through A+B combinations
        for i in range(N):
            for j in range(N):
                if -1 * (A[i] + B[j]) in cd:
                    res += cd[-1 * (A[i] + B[j])]
        return res
    
    