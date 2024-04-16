class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, x2, y1, y2 = rec1[0], rec1[2], rec1[1], rec1[3]
        xx1, xx2, yy1, yy2 = rec2[0], rec2[2], rec2[1], rec2[3]
        
        # edge cases
        if x1 == x2 or y1 == y2 or xx1 == xx2 or yy1 == yy2:
            return False
        
        con1 = (x1 < xx2) and (yy1 < y1 < yy2 or yy1 < y2 < yy2) and (x2 > xx1)
        con2 = (xx1 < x2) and (y1 < yy1 < y2 or y1 < yy2 < y2) and (xx2 > x1)
        return con1 or con2
        
        
        