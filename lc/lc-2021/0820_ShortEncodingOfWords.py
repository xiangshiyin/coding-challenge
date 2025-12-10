# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         '''
#         O(mn) in time and O(mn) in space
#         '''
#         ans = 0
#         seen = set()

#         # sort words by length
#         words.sort(key = lambda x: -len(x))
#         # print(words)


#         for w in words:
#             if w not in seen:
#                 ans += len(w) + 1
#             seen = seen | set([w[i:] for i in range(len(w))])

#         return ans

# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         '''
#         lc solution # 1
#         '''
#         good = set(words)
#         for word in words:
#             for k in range(1, len(word)):
#                 good.discard(word[k:]) # discard is better than remove

#         return sum(len(word) + 1 for word in good)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        lc solution # 2
        """
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]

        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)
