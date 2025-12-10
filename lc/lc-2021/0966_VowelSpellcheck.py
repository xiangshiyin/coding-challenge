class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        build 3 hash tables
        1. the raw wordlist
        2. the case normalized wordlist
        3. the wordlist with vowels removed
        """

        tb1 = set(wordlist)

        tb2 = {}
        for w in wordlist:
            if w.lower() not in tb2:
                tb2[w.lower()] = w

        tb3 = {}
        for w in wordlist:
            w2 = "".join([char if char not in "aeiou" else "," for char in w.lower()])
            if w2 not in tb3:
                tb3[w2] = w

        ans = ["" for i in range(len(queries))]

        for ix, q in enumerate(queries):
            q2 = q.lower()
            q3 = "".join(
                [char if char not in "aeiouAEIOU" else "," for char in q.lower()]
            )
            if q in tb1:
                ans[ix] = q
            elif q2 in tb2:
                ans[ix] = tb2[q2]  # 1st of such in rawlist
            elif q3 in tb3:
                ans[ix] = tb3[q3]  # 1st of such in rawlist

        return ans
