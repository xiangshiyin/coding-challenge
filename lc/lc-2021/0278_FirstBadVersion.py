# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n - 1
        first = n
        while l <= r:
            if l == n:
                return l

            m = (l + r) // 2
            if isBadVersion(m):
                first = m
                r = m - 1
            else:
                l = m + 1
        return first
