class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        '''
        Sort A, search value in A for every B
        '''
        A.sort()
        
        from collections import defaultdict
        tb = defaultdict(list)
        for b in sorted(B, reverse=True):
            if b < A[-1]:
                tb[b].append(A.pop())
        
        return [(tb[b] or A).pop() for b in B]
    
    