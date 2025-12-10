# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # find the unique combinations while traversing the list
#         from collections import defaultdict
#         tb = defaultdict(list)
#         for v in strs:
#             tb[''.join(sorted(v))].append(v)
#         # print(tb)

#         return [tb[key] for key in tb]


class Solution:
    """
    Solution without sort
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreqSeq(s):
            freqs = [0] * 26
            for char in s:
                freqs[ord(char) - ord("a")] += 1
            return tuple(freqs)

        from collections import defaultdict

        tb = defaultdict(list)

        for v in strs:
            tb[getFreqSeq(v)].append(v)

        return [tb[key] for key in tb]
