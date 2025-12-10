class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1s = [int(v) for v in version1.split(".")]
        v2s = [int(v) for v in version2.split(".")]
        # print(v1s, v2s)

        ## clean trailing 0s
        while not v1s[-1] and len(v1s) > 1:
            v1s.pop()
        while not v2s[-1] and len(v2s) > 1:
            v2s.pop()

        n1 = len(v1s)
        n2 = len(v2s)
        ix = 0
        jx = 0
        while ix < n1 and jx < n2:
            if v1s[ix] < v2s[jx]:
                return -1
            elif v1s[ix] > v2s[jx]:
                return 1
            else:
                ix += 1
                jx += 1

        if ix == jx and ix == n1 and jx == n2:
            return 0
        elif ix < n1:
            return 1
        else:
            return -1
