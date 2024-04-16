class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        m = len(relations)
        
        from collections import defaultdict
        dg_in = defaultdict(int)
        start2end = defaultdict(list)
        
        # initialize dg_in, start2end
        for start,end in relations:
            dg_in[end] += 1
            start2end[start].append(end)
            
        from collections import deque
        q = deque()
        step = 0
        counter = 0
        
        # initialize the queue
        for start in range(1, n+1):
            if dg_in[start] == 0:
                q.append(start)

        # print(q)
        
        while q:
            step += 1
            len_q = len(q)
            ix = 0
            
            while ix < len_q:
                start = q.popleft()
                counter += 1
                ends = start2end[start]
                for end in ends:
                    dg_in[end] -= 1
                    if dg_in[end] == 0:
                        q.append(end)
                ix += 1
        
        if counter < n:
            return -1
        else:
            return step
        
                
            
            
            
        
        
        
        