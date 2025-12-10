class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        # exceptions
        if n == 0:
            return ""
        elif n == 1:
            return strs[0]

        # traverse the list
        ans = strs[0]
        ix = 1
        while ix < n:
            jx = 0
            while jx < len(strs[ix]) and jx < len(ans) and strs[ix][jx] == ans[jx]:
                jx += 1
            if jx == 0:
                return ""
            else:
                ans = ans[:jx]

            ix += 1

        return ans
