# class Solution:
#     def findLongestWord(self, s: str, d: List[str]) -> str:
#         '''
#         with pre-sorting
#         '''
#         # sort the word list by length and lexicographical order
#         d1 = sorted(d, key = lambda x: (-1 * len(x), x))
        
#         for w in d1:
#             p1 = 0
#             p2 = 0
#             while p1 < len(s) and p2 < len(w):
#                 while p1 < len(s) and s[p1] != w[p2]:
#                     p1 += 1
#                 if p1 < len(s):
#                     p1 += 1
#                     p2 += 1
#                 else:
#                     break
#             if p2 < len(w):
#                 continue
#             else:
#                 return w
        
#         return ""
        
        
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        '''
        with pre-sorting
        '''
        result = ''
        
        for w in d:
            p1 = 0
            p2 = 0
            while p1 < len(s) and p2 < len(w):
                while p1 < len(s) and s[p1] != w[p2]:
                    p1 += 1
                if p1 < len(s):
                    p1 += 1
                    p2 += 1
                else:
                    break
            if p2 < len(w):
                continue
            else:
                if len(w) > len(result):
                    result = w
                elif len(w) == len(result) and w < result:
                    result = w
        
        return result
        
        
        
        