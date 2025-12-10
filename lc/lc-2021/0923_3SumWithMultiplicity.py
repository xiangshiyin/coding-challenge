# class Solution:
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         '''
#         Time limit exceeded, O(n2)
#         '''
#         m = len(arr)

#         # create a hash table to record pairwise sum info
#         from collections import defaultdict
#         tb = defaultdict(dict)
#         for ix in range(m-1):
#             for jx in range(ix+1,m):
#                 # print((ix,jx), arr[ix] + arr[jx])
#                 if arr[ix] + arr[jx] not in tb[ix]:
#                     tb[ix][arr[ix] + arr[jx]] = 1
#                 else:
#                     tb[ix][arr[ix] + arr[jx]] += 1
#         # print(tb)

#         # 2nd pass, populate the counter
#         counter = 0
#         for ix in range(m-1):
#             for jx in range(ix+1,m):
#                 if arr[ix] + arr[jx] <= target:
#                     if target - arr[ix] in tb[jx]:
#                         counter += tb[jx][target - arr[ix]]
#         return int(counter % (1e9 + 7))


class Solution(object):
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        from collections import Counter

        tb = Counter(arr)

        ans = 0
        arr2 = list(tb.keys())
        m = len(arr2)

        for v1 in arr2:
            for v2 in arr2:
                if v1 < v2 < target - v1 - v2:
                    ans += tb[v1] * tb[v2] * tb[target - v1 - v2]

        for v in arr2:
            if tb[v] > 1 and target - 2 * v in tb:
                if v != target - 2 * v:
                    ans += tb[v] * (tb[v] - 1) * (1 / 2) * tb[target - 2 * v]
                else:
                    ans += tb[v] * (tb[v] - 1) * (tb[v] - 2) * (1 / 6)

        return int(ans % (10**9 + 7))
