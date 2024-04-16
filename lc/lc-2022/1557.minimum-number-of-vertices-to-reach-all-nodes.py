#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set([e[0] for e in edges]) - set([e[1] for e in edges]))


# @lc code=end
