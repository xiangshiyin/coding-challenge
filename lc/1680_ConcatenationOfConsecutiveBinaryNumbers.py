class Solution:
    def concatenatedBinary(self, n: int) -> int:
        shift = 0
        i = 1
        output = 0
        
        while i <= n:
            if i & (i-1) == 0:
                shift = shift + 1
            output = ((output << shift) | i) % (10**9 + 7)

            i += 1
        
        return output
