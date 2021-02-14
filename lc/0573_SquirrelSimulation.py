class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        '''
        only beats 7% in time
        '''
        # step 0: define a utility function to calculate distance
        def getDist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        # step 1: do the calculation
        n2t_round = sum([getDist(nut, tree) * 2 for nut in nuts]) # nut to tree round trip
        
        dist = min([getDist(nut, squirrel) - getDist(nut, tree) + n2t_round for nut in nuts])
        return dist
            

             
        
        
        
        