class Solution:
    def intToRoman(self, num: int) -> str:
        bases = [1000, 100, 10, 1]
        symbols = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        ans = ""

        ibase = 0
        while num > 0:
            while ibase < len(bases) and num // bases[ibase] == 0:
                ibase += 1
            factor = num // bases[ibase]
            num = num % bases[ibase]

            if factor < 4:
                ans += symbols[bases[ibase]] * factor
            elif factor == 4:
                ans += symbols[bases[ibase]] + symbols[bases[ibase] * 5]
            elif factor == 5:
                ans += symbols[bases[ibase] * 5]
            elif factor < 9:
                ans += symbols[bases[ibase] * 5] + symbols[bases[ibase]] * (factor - 5)
            else:
                ans += symbols[bases[ibase]] + symbols[bases[ibase] * 10]
        return ans
