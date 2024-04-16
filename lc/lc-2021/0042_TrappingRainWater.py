class Solution:
    def trap(self, height: List[int]) -> int:
        # exceptions
        if height==None:
            return 0
        N = len(height)
        if N<=2:
            return 0
        # traverse the list
        left = 0
        right = N-1
        lmax = 0
        rmax = 0
        volume = 0
        
        while left <= right:
            if height[left]>lmax:
                lmax = height[left]
            if height[right]>rmax:
                rmax = height[right]
            if rmax<=lmax:
                volume += rmax-height[right]
                right -= 1
            else:
                volume += lmax-height[left]
                left += 1
        return volume
        
        