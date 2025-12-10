# class Solution:
#     def minDeletions(self, s: str) -> int:
#         from collections import Counter
#         freq = Counter(s)
#         l = sorted([freq[k] for k in freq], reverse = True)
#         # print(l)

#         ans = 0
#         for i in range(1, len(l)):
#             if l[i] == l[i-1]:
#                 ans += 1
#                 l[i] -= 1
#             elif l[i] > l[i-1]:
#                 if l[i-1] > 0:
#                     ans += l[i] - l[i-1] + 1
#                     l[i] -= l[i] - l[i-1] + 1
#                 else:
#                     ans += l[i]
#                     l[i] -= l[i]
#         return ans


class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        l = sorted([freq[k] for k in freq], reverse=True)

        ans = 0
        seen = set()
        for f in l:
            while f in seen:
                f -= 1
                ans += 1
            if f:
                seen.add(f)
        return ans
