class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        '''
        Greedy
        '''
        step = 0
        if X > Y:
            return X - Y
        elif X == Y:
            return 0
        else:
            while X < Y:
                if Y % 2 == 0:
                    Y = Y // 2
                    step += 1
                else:
                    Y += 1
                    step += 1
            if X == Y:
                return step
            else:
                return step + (X - Y)
            
