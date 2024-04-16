class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        from collections import Counter
        freq = Counter(data)
        
        # special cases
        if n <= 2 or len(freq) == 1 or freq[1] == 1:
            return 0
        
        # define a window whose length is the same as the number of 1s in the list
        # move the window from left to right such that the number of 1s in the window is maximized
        l = 0
        r = freq[1]
        ones_max = sum(data[l:r])
        ones = sum(data[l:r])
        while r <= n:
            if r > freq[1]:
                l = r - freq[1]
                ones -= data[l - 1] - data[r - 1]
                ones_max = max(ones_max, ones)
            r += 1
        
        return freq[1] - ones_max
    
    