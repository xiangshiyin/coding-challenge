# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         counter = 0
#         while n > 0:
#             counter += n & 1
#             n = n >> 1
#         return counter


class Solution:
    """
    n & n - 1 trick
    """

    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n > 0:
            n = n & (n - 1)
            counter += 1
        return counter
