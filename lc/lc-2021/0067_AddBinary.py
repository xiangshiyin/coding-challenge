# class Solution:
#     '''
#     bit manipulations
#     '''
#     def addBinary(self, a: str, b: str) -> str:
#         m = len(a)
#         n = len(b)

#         a2 = 0
#         i = 0
#         while i < m:
#             if a[m - 1 -i] == '1':
#                 a2 += 1 << i
#             i += 1

#         b2 = 0
#         i = 0
#         while i < n:
#             if b[n - 1 - i] == '1':
#                 b2 += 1 << i
#             i += 1

#         total = a2 + b2
#         if not total:
#             return '0'

#         i = 0
#         while total:
#             total = total >> 1
#             i += 1

#         marker = 1 << (i - 1)
#         ans = ''
#         total = a2 + b2

#         while marker:
#             if total & marker:
#                 ans = ans + '1'
#             else:
#                 ans = ans + '0'
#             marker = marker >> 1

#         return ans


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        delta = 0
        l1 = list(a)
        l2 = list(b)
        ans = ""

        while l1 or l2 or delta:
            if l1:
                delta += int(l1.pop())
            if l2:
                delta += int(l2.pop())

            ans = str(delta % 2) + ans
            delta = delta // 2
        return ans
