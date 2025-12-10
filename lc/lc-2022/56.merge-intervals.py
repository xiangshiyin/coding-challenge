#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by starting index
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if i == 0:
                ans.append(intervals[i])
            else:
                if intervals[i][0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                else:
                    ans.append(intervals[i])
        return ans


# @lc code=end
