class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)
        counter = 0
        for s in stones:
            if s in jset:
                counter += 1
        return counter
