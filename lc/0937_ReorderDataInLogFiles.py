# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         '''
#         heap sort
#         '''
#         from heapq import heappush, heappop
#         hp = []
        
#         for i,log in enumerate(logs):
#             # check the log type
#             if log[log.index(' ') + 1].isnumeric(): # digital log
#                 # (1, 1, i) represents (type, content, identifier), digital logs all have (1, 1, i) label
#                 heappush(hp, (1, 1, i)) 
#             else: # letter log
#                 heappush(hp, (0, log[log.index(' ') + 1 : ], log[ : log.index(' ')]))
        
#         # generate the answer
#         ans = []
#         for i in range(len(hp)):
#             tp, ct, idf = heappop(hp)
#             if tp == 1 and ct == 1:
#                 ans.append(logs[idf])
#             else:
#                 ans.append(f'{idf} {ct}')
        
#         return ans
    
        
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        use the built-in sort() function
        '''
        def get_key(log):
            idf, ct = log.split(maxsplit=1)
            return (0, ct, idf) if ct[0].isalpha() else (1, 1, 1)
        
        return sorted(logs, key=get_key)
    

