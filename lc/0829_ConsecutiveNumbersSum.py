class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        pure math solution
        n = (0 + k) + (1 + k) + (2 + k) + ... + (m + k)
        Therefore, n = (m + 1) * (m + 2k) / 2
        m could be anything from 1 to int(((1 + 8n) ** (1/2) - 3)/2)
        '''
        
        counter = 0
        import math
        m_upper = int((math.sqrt(1 + 8 * N) - 3) / 2) + 1
        
        for m in range(m_upper):
            if ((2 * N) / (m + 1) - m) // 2 >= 0 and ((2 * N) / (m + 1) - m) % 2 == 0:
                counter += 1
                
        return counter
        
        
        
        