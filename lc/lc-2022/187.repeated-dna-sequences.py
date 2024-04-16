#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         from collections import defaultdict

#         saw = set()
#         res = set()
#         for i in range(len(s) - 9):
#             if s[i : i + 10] not in saw:
#                 saw.add(s[i : i + 10])
#             else:
#                 res.add(s[i : i + 10])
#         return list(res)


# solution on 2022-09-26
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        numeric representation of string, 四进制
        """
        l = r = 0
        curr = 0
        saw = set()
        ans = set()
        while r < len(s):
            curr = curr * 4 + self.encode(s[r])
            if r - l + 1 == 10:
                if s[l : r + 1] in saw:
                    ans.add(s[l : r + 1])
                else:
                    saw.add(s[l : r + 1])
                curr = curr - self.encode(s[l]) * (4**9)
                l += 1
            r += 1
        return list(ans)

    def encode(self, s):
        if s == "A":
            return 0
        elif s == "C":
            return 1
        elif s == "G":
            return 2
        else:
            return 3


# @lc code=end
