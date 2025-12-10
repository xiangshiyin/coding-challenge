class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        # self.board = [[0] * n for i in range(n)]
        # use an array of length 2n + 2 to represent the status of each player
        # 1st row for player 1, 2nd row for player 2
        # the sequence: n rows, n columns, upperleft->lowerright, lowerleft->upperright
        self.status = [[0] * (2 * n + 2) for i in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # # update the game board
        # self.board[row][col] = player

        # update the player status
        self.status[player - 1][row] += player
        self.status[player - 1][self.n + col] += player
        if row == col:
            self.status[player - 1][2 * self.n] += player
        if row == self.n - 1 - col:
            self.status[player - 1][2 * self.n + 1] += player

        # update game status
        if (
            self.status[player - 1][row] == self.n * player
            or self.status[player - 1][self.n + col] == self.n * player
            or self.status[player - 1][2 * self.n] == self.n * player
            or self.status[player - 1][2 * self.n + 1] == self.n * player
        ):
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
