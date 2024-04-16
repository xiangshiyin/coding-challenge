# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         n1 = len(num1)
#         n2 = len(num2)
#         tb = {str(i):i for i in range(10)}
#         ans = 0
#         delta = 0
        
#         for i in range(min(n1,n2)):
#             tmp = tb[num1[n1 - 1 - i]] + tb[num2[n2 - 1 - i]] + delta
#             ans += (tmp % 10) * (10 ** i)
#             delta = tmp // 10
        
#         if min(n1, n2) == n1:
#             i += 1
#             while i < n2:
#                 tmp = tb[num2[n2 - 1 - i]] + delta
#                 ans += (tmp % 10) * (10 ** i)
#                 delta = tmp // 10
#                 i += 1
#         else:
#             i += 1
#             while i < n1:
#                 tmp = tb[num1[n1 - 1 - i]] + delta
#                 ans += (tmp % 10) * (10 ** i)
#                 delta = tmp // 10
#                 i += 1
#         if delta > 0:
#             return str(ans + delta * (10 ** (i))) 
        
#         return str(ans)
            
        
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        tb = {str(i):i for i in range(10)}
        ans = ''
        delta = 0
        
        ix = 0
        while ix < max(n1, n2):
            v1 = tb[num1[n1 - 1 - ix]] if ix < n1 else 0
            v2 = tb[num2[n2 - 1 - ix]] if ix < n2 else 0
            tmp = v1 + v2 + delta
            ans = str(tmp % 10) + ans
            delta = tmp // 10
            ix += 1
        
        if delta:
            ans = str(delta) + ans 
        
        return ans
    