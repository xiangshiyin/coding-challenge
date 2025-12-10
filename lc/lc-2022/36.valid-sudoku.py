#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if (
                    board[i][j] not in rows[i]
                    and board[i][j] not in cols[j]
                    and board[i][j] not in subs[3 * (i // 3) + j // 3]
                ):
                    if board[i][j] != ".":
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        subs[3 * (i // 3) + j // 3].add(board[i][j])
                else:
                    return False
        return True


# @lc code=end
