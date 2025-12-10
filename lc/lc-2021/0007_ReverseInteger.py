class Solution:
    def reverse(self, x: int) -> int:
        # exception
        if x == 0:
            return 0

        v = abs(x)
        sign = 1 if v == x else -1
        ans = 0
        i = 0

        while v > 0:
            tmp = v % 10
            ans = ans * 10 + tmp
            v = v // 10
            i += 1
        # print(ans)

        if -(2**31) <= ans * sign <= 2**31 - 1:
            return ans * sign
        else:
            return 0
