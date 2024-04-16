# class Solution:
#     def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
#         '''
#         Time limit exceeded
#         '''
#         from collections import Counter
#         dictA = [Counter(a) for a in A]
#         dictB = [Counter(b) for b in B]
        
#         na = len(A)
#         nb = len(B)
#         ans = []
#         for i in range(na):
#             flg = 1
#             for j in range(nb):
#                 for lb in dictB[j].keys():
#                     if lb not in dictA[i] or dictB[j][lb] > dictA[i][lb]:
#                         flg = 0
#                         break
#                 if flg == 0:
#                     break
#             if flg == 1:
#                 ans.append(A[i])
        
#         return ans
                

# class Solution:
#     def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
#         '''
#         Time limit exceeded
#         '''
#         from collections import Counter
#         dictA = [Counter(a) for a in A]
#         dictB = [Counter(b) for b in B]
        
#         na = len(A)
#         nb = len(B)
#         ans = []
#         for i in range(na):
#             counter = 0
#             for j in range(nb):        
#                 tmp =  sum([1 if dictA[i][l] >= dictB[j][l] else 0 for l in dictB[j]])
#                 if tmp == len(dictB[j]):
#                     counter += 1
#             if counter == nb:
#                 ans.append(A[i])
#         return ans
        
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        from collections import Counter
        countB = Counter()
        
        for b in B:
            countB = countB | Counter(b)
            
        return [a for a in A if not countB - Counter(a)]

            
        
        
        
