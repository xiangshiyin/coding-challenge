class Solution:
    def climbStairs(self, n: int) -> int:
        """
        it all depends on the size of the last step achieving (n - 1)
        climbStairs(n) = climbStairs(n-1, ends with 2 step) + climbStairs(n-1, ends with 1 step) * 2

        and:
        climbStairs(n, ends with 2 step) = climbStairs(n-1, ends with 1 step)
        climbStairs(n, ends with 1 step) = climbStairs(n-1, ends with 1 step) + climbStairs(n-1, ends with 2 step)
        """
        ways = [1, 0]  # [ways end with 1 step, ways end with 2 step]
        if n == 1:
            return ways[0] + ways[1]
        else:
            for i in range(2, n + 1):
                old_1step = ways[0]
                ways[0] = ways[0] + ways[1]
                ways[1] = old_1step

            return ways[0] + ways[1]
