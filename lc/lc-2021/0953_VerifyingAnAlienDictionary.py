class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # exceptions
        if len(words) == 1:
            return True

        # build the lookup table on lexicographical order
        tb = {letter: idx for idx, letter in enumerate(order)}

        # traverse the words and check the order
        l = 0
        r = 1
        while r < len(words):
            # locate the words
            lw = words[l]
            rw = words[r]
            # define inner pointers
            li = 0
            ri = 0
            while li < len(lw) and ri < len(rw):
                if tb[lw[li]] > tb[rw[ri]]:
                    return False
                elif tb[lw[li]] < tb[rw[ri]]:
                    break
                else:
                    li += 1
                    ri += 1
            if li < len(lw) and ri == len(rw):
                return False
            # the two words follow the right order
            l = r
            r += 1
        return True


## on 4/9/2021, new solution
# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         lx = {l:i for i,l in enumerate(order)}
#         n = len(words)
#         # special case
#         if n==1:
#             return True

#         def helper(w1, w2):
#             n1 = len(w1)
#             n2 = len(w2)
#             p1 = 0
#             p2 = 0
#             while p1 < n1 and p2 < n2:
#                 if lx[w1[p1]] < lx[w2[p2]]:
#                     return True
#                 elif lx[w1[p1]] > lx[w2[p2]]:
#                     return False
#                 else:
#                     p1 += 1
#                     p2 += 1
#             if p1 < n1:
#                 return False
#             if p2 < n2:
#                 return True
#             return True


#         for i in range(1,n):
#             if not helper(words[i-1],words[i]):
#                 return False
#         return True
