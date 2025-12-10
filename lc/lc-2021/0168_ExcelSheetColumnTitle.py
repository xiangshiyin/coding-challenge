class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        num = columnNumber

        # create a lookup table
        tb = {n: l for l, n in zip(list("ZABCDEFGHIJKLMNOPQRSTUVWXY"), list(range(26)))}
        # print(tb)

        while num >= 0:
            ans = tb[num % 26] + ans
            # update num
            if num <= 26:
                break
            else:
                if num % 26 > 0:
                    num = num // 26
                else:
                    num = (num - 26) // 26

        return ans
