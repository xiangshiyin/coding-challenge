#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        if not trust and n == 1:
            return 1

        from collections import defaultdict

        stats = defaultdict(int)
        seen = set()
        ans = -1
        counter = 0
        for t in trust:
            stats[t[1]] += 1
            seen.add(t[0])

        for k, v in stats.items():
            if v == n - 1 and k not in seen:
                ans = k
                counter += 1
        return ans if counter == 1 else -1


# @lc code=end
