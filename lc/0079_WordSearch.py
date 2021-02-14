class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        # plan for the steps
        self.steps = [[0,1],[1,0],[0,-1],[-1,0]]
        
        # traverse the matrix
        for i in range(self.m):
            for j in range(self.n):
                if self.backtrack(i,j,word):
                    return True
            
        return False
                
    # the backtrack logic
    def backtrack(self, row, col, suffix):
        if len(suffix)==0:
            return True
        if row<0 or row==self.m or col<0 or col==self.n or self.board[row][col]!=suffix[0]:
            return False

        self.board[row][col] = '#'
        for rowOffset,colOffset in self.steps:
            result = self.backtrack(row+rowOffset, col+colOffset, suffix[1:])
            if result:
                break
        self.board[row][col] = suffix[0]
        return result
                    
                
            
        
        