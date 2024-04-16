class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        l = 0
        r = n - 1
        v = 0
        while l < r:
            h = min(height[l], height[r])
            v_curr = h * (r - l)
            v = max(v, v_curr)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return v
    