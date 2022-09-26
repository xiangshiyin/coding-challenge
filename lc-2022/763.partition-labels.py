#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        # collect all the intervals
        intervals = {}
        for i, ch in enumerate(s):
            if ch not in intervals:
                intervals[ch] = [i, i]
            else:
                intervals[ch][1] = i
        # sort the intervals
        intervals2 = sorted(intervals.values(), key=lambda x: (-x[1], x[0]))

        # traverse the intervals
        currL = 0
        prev_l = intervals2[0][0]
        prev_h = intervals2[0][1]
        curr = 0
        while curr < len(intervals2):
            if curr == 0:
                currL += intervals2[curr][1] - intervals2[curr][0] + 1
            else:
                if intervals2[curr][1] <= prev_l:
                    ans.append(currL)
                    currL = intervals2[curr][1] - intervals2[curr][0] + 1
                    prev_l = intervals2[curr][0]
                    prev_h = intervals2[curr][1]
                else:
                    prev_l = min(prev_l, intervals2[curr][0])
                    currL = prev_h - prev_l + 1
            curr += 1

        ans.append(currL)

        return ans[::-1]


# @lc code=end
