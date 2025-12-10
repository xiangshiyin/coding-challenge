class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        n = len(S)

        # exceptions
        if n <= 1:
            return S

        pool = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # one pointer
        nonletter = []
        r = n - 1
        tmp = ""
        while r >= 0:
            if S[r] in pool:
                tmp += S[r]
            else:
                nonletter.append(r)
            r -= 1

        # print(nonletter)
        # print(tmp)

        # format the output
        ans = ""
        len_curr = 0
        prev = 0
        for ix in nonletter[::-1]:
            ans += tmp[prev : prev + ix - len_curr] + S[ix]
            prev = prev + ix - len_curr
            len_curr = ix + 1
            # print(ans)
        ans += tmp[prev:]

        return ans
