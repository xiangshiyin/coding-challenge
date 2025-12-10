class Solution:
    def numberToWords(self, num: int) -> str:
        # print(1 << 31 - 1)

        # special case
        if num == 0:
            return "Zero"

        # create mapping table
        ws = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred Thousand Million Billion"
        nums = (
            list(range(1, 20))
            + list(range(20, 91, 10))
            + [100, 1000, 1000000, 1000000000]
        )
        tb = {num: w for num, w in zip(nums, ws.split())}
        # print(tb)

        # break by thousands
        v = num
        ts = []
        while v > 0:
            ts.append(v % 1000)
            v = v // 1000

        # traverse the list and generate the answer
        ans = ""
        for i in range(len(ts)):
            t = ts[i]
            if t > 0:
                hundreds = t // 100
                tens = (t % 100 // 10) * 10
                ones = t % 10
                tmp = ""
                if hundreds > 0:
                    tmp += tb[hundreds] + " Hundred"
                if 0 < t % 100 <= 20:
                    tmp += " " + tb[t % 100] if hundreds > 0 else tb[t % 100]
                else:
                    if tens > 0:
                        tmp += " " + tb[tens] if hundreds > 0 else tb[tens]
                    if ones > 0:
                        tmp += " " + tb[ones] if tens > 0 else tb[ones]
                if i == 0:
                    ans += tmp
                else:
                    ans = (
                        tmp + " " + tb[1000**i] + " " + ans
                        if len(ans) > 0
                        else tmp + " " + tb[1000**i]
                    )
            # print(hundreds, tens, ones, ans)

        return ans
