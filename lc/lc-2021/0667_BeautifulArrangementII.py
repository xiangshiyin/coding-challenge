class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []

        # construct the series with k unique differences
        for i in range(1, k + 2):
            if i % 2 == 1:
                ans.append(i // 2 + 1)
            else:
                ans.append(k - i // 2 + 2)
        # append the residuals
        for i in range(k + 2, n + 1):
            ans.append(i)

        return ans
