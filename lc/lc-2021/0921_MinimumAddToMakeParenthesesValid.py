class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        N = len(S)
        # exceptions
        if N <= 1:
            return N

        # traverse the string from left to right
        lcounter = 0
        rcounter = 0
        toadd = 0

        for char in S:
            if char == "(":
                lcounter += 1
            else:
                rcounter += 1

            if rcounter > lcounter:
                toadd += rcounter - lcounter
                lcounter = 0
                rcounter = 0

        toadd += lcounter - rcounter

        return toadd
