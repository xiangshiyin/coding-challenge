#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            cur = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    tmp = output[i - 1][j - 1] + output[i - 1][j]
                    cur.append(tmp)
            output.append(cur)
        return output


# @lc code=end
