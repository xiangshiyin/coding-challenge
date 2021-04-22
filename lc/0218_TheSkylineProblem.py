class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        only need to consider adjacent buildings
        '''
        n = len(buildings)
        
        bs = [(l, -h, r) for l, r, h in buildings] + [(r, 0, r) for l, r, h in buildings]
        bs.sort()
        
        from heapq import heappush, heappop
        hp, res = [(0, float('inf'))], [[0, 0]]
        for l, h, r in bs:
            while hp[0][1] <= l: # need to clear out when reaching then end of max block or starting a new block
                heappop(hp)
            if h:
                heappush(hp, (h, r))
            if res[-1][1] != -hp[0][0]:
                res += [[l, -hp[0][0]]]
            # print(l, h, r, hp, res)
        return res[1:]
    
        
        
        
                        
                    
        
        
        
        