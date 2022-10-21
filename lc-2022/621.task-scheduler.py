#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import heapq

        freq = Counter(tasks)
        pool = []
        for k, v in freq.items():
            heapq.heappush(pool, (-v, k))

        time = 0
        cache = []
        while pool or cache:
            if pool:
                n_f, candidate = heapq.heappop(pool)  # n_f = "negative frequency"
                if n_f + 1 < 0:
                    cache.append((n_f + 1, candidate))
            time += 1
            if time % (n + 1) == 0:
                while cache:
                    heapq.heappush(pool, cache.pop())

        return time


# @lc code=end
