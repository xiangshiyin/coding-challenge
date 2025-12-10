class Solution:
    def myAtoi(self, s: str) -> int:
        lb = -1 * (1 << 31)  # lower bound
        ub = (1 << 31) - 1  # upper bound
        # print(lb, ub)

        ix = 0
        while ix < len(s) and s[ix] == " ":
            ix += 1
        if ix == len(s) or (s[ix] not in ("-", "+") and not s[ix].isnumeric()):
            return 0

        sign = 1 if s[ix] == "+" or s[ix].isnumeric() else -1

        if not s[ix].isnumeric():
            ix += 1

        num = ""
        while ix < len(s) and s[ix].isnumeric():
            num += s[ix]
            ix += 1

        if num == "":
            return 0
        else:
            res = sign * int(num)
            if lb <= res <= ub:
                return res
            elif res < lb:
                return lb
            else:
                return ub
