class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num = len(set(candyType))
        n = len(candyType) // 2

        return min(num, n)
