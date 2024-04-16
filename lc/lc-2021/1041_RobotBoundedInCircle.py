class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        check if the robot changes direction after one iteration
        '''
        lnext = {
            (0,1):(-1,0),
            (-1,0):(0,-1),
            (0,-1):(1,0),
            (1,0):(0,1)
        }
        rnext = {
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1)
        }
        
        ix = 0
        d = (0,1)
        p = (0,0)
        flg = 0 # if there is a direction instruction
        while ix < len(instructions):
            while ix < len(instructions) and instructions[ix] == 'G':
                p = (p[0] + d[0], p[1] + d[1])
                ix += 1
            if ix < len(instructions):
                d = lnext[d] if instructions[ix] == 'L' else rnext[d]
                flg = 1
            else:
                break
            ix += 1
        
        print(flg)
        
        if not flg or (p != (0,0) and d == (0,1)):
            return False
        else:
            return True
            
        
        
        