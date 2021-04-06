# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         n = len(target)
#         m = len(stamp)
#         t = list(target)
#         s = list(stamp)
#         ans = []
        
#         def check(ix):
#             found = False
#             for jx in range(m):
#                 if t[ix + jx] == '?':
#                     continue
#                 if t[ix + jx] != s[jx]:
#                     return False
#                 found = True
#             if found:
#                 t[ix:ix+m] = ['?'] * m
#                 ans.append(ix)
#             return found
        
#         found = True
#         while found:
#             found = False
#             for i in range(n - m + 1):
#                 found = found | check(i)
        
#         print(ans, t)
        
#         if t == ['?'] * n:
#             return ans[::-1]
#         else:
#             return []

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        '''
        redo the problem on 4/1/2021
        '''
        ls = len(stamp)
        lt = len(target)
        s = list(stamp)
        t = list(target)
        ans = []
        
        def check(ix):
            flg = 0
            for jx in range(ls):
                if t[ix + jx] == '?':
                    continue
                if t[ix + jx] != s[jx]:
                    return 0
                elif t[ix + jx] == s[jx]:
                    flg = 1
            if flg:
                t[ix:ix+ls] = ['?'] * ls
                ans.append(ix)
            return flg
        
        found = 1
        while found:
            found = 0
            for i in range(lt - ls + 1):
                found = found | check(i)
        print(ans)
        
        if t == ['?'] * lt:
            return ans[::-1]
        else:
            return []
        
        
        
        
        
        