class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0

        def helper(ix, prefix):
            if ix == len(arr) or len(set(arr[ix])) < len(arr[ix]):
                return
            if len(set(arr[ix]) & set(prefix)) == 0:
                prefix += arr[ix]
                self.ans = max(self.ans, len(prefix))
            else:
                return

            for jx in range(ix + 1, len(arr)):
                helper(jx, prefix)

        for i in range(len(arr)):
            helper(i, "")

        return self.ans
