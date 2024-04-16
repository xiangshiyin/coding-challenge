class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        # generate random theta value
        import random
        import math
        
        theta = random.uniform(0, 2 * math.pi)
        R = self.r * math.sqrt(random.uniform(0,1))
        
        x = R * math.cos(theta)
        y = R * math.sin(theta)
        return [self.x + x, self.y + y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
