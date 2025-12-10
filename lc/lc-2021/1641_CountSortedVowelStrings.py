class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        brutal force recursion
        """
        # create a pool for later loops
        source = ["a", "e", "i", "o", "u"]
        pool = {source[i]: source[i:] for i in range(5)}

        # start from different letters
        def helper(start, m):
            counter = 0
            if m == 1:
                return len(pool[start])
            else:
                for char in pool[start]:
                    counter += helper(char, m - 1)
                return counter

        return helper("a", n)
