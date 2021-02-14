# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         '''
#         Solution with heap implementation
#         '''
        
#         # create a lookup table
#         import string
#         # tb1 = {(i+1):char for i,char in enumerate(string.ascii_lowercase)}
        
#         # exception
#         if n==1:
#             return string.ascii_lowercase[k-1]
        
#         import heapq
#         hp = [1 for i in range(n)]
#         heapq.heapify(hp)
#         total = n
        
#         while total <= k:
#             if total == k:
#                 return ''.join([string.ascii_lowercase[heapq.heappop(hp)-1] for i in range(n)])
#             if k - total > 26:
#                 out = heapq.heappushpop(hp, 26)
#                 total = total - out + 26
#             else:
#                 out = heapq.heappop(hp)
#                 total -= out
#                 if k - total > 26:
#                     heapq.heappush(hp, 26)
#                     total += 26
#                 else:
#                     heapq.heappush(hp, k - total)
#                     total += (k - total)
                    
# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         '''
#         Solution with simple loop, one pass. Memory about the same, run time much shorter
#         '''
#         source = 'abcdefghijklmnopqrstuvwxyz'
#         raw = [1 for i in range(n)]
#         total = n
        
#         i = n-1
#         while i >= 0:
#             if total == k:
#                 return ''.join([source[v-1] for v in raw])
            
#             if k - total > 26:
#                 total -= raw[i]
#                 raw[i] = 26
#                 total += 26
#             else:
#                 total -= raw[i]
#                 if k - total > 26:
#                     raw[i] = 26
#                     total += raw[i]
#                 else:
#                     raw[i] = k - total
#                     total += k - total
#             i -= 1
#         return ''.join([source[v-1] for v in raw]) 

# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         '''
#         Solution with direct accumulation, much less memory, but still long run time
#         '''
#         source = 'abcdefghijklmnopqrstuvwxyz'
#         output = ''
#         total = 0
        
#         i = n-1
#         while i >= 0:
#             if total == k:
#                 return output
            
#             if k - i - total > 26:
#                 output =  'z' + output
#                 total += 26
#             else:
#                 output = source[k - i - total - 1] + output
#                 total += k - i - total
                
#             i -= 1
        
#         return output
            
class Solution:
    def getSmallestString(self, n, k):
        source = 'abcdefghijklmnopqrstuvwxyz'
        num_z = (k - n) // 25
        
        print(num_z)
        
        if (k - n) % 25 == 0:
            return 'a' * (n - num_z) + 'z' * num_z
        else:
            return 'a' * (n - num_z - 1) + source[(k - n) % 25] + 'z' * num_z
        
        
        
            
            
            
            
            
            
    