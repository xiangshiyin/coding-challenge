#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex + 1):
            curr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(curr)
        return curr


# @lc code=end
