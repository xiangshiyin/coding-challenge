class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        
        counter = 0
        for row in range(m):
            for col in range(n):
                if row == 0:
                    if board[row][col] == 'X':
                        if col == 0 or board[row][col - 1] == '.':
                            counter += 1
                else:
                    if board[row][col] == 'X':
                        if (col == 0 or board[row][col - 1] == '.') and board[row - 1][col] == '.':
                            counter += 1
            # print(counter)
        return counter
            