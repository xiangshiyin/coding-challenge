# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        non_candidate = set()
        for i in range(n):
            if i != candidate and knows(candidate, i) == 1:
                candidate = i

        for j in range(n):
            if j != candidate and (knows(candidate, j) == 1 or not knows(j, candidate)):
                return -1

        return candidate
