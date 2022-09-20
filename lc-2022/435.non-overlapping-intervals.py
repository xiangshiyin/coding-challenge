#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # exceptions
        if len(intervals) == 1:
            return 0

        # sort the intervals by the end position
        intervals.sort(key=lambda intv: intv[1])
        prev = 0
        curr = 1
        counter = 1
        while curr < len(intervals):
            if intervals[curr][0] >= intervals[prev][1]:
                counter += 1
                prev = curr
            curr += 1
        return len(intervals) - counter


# @lc code=end

