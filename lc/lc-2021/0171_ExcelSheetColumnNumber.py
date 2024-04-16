class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # create a lookup table
        tb = {
            l:n
            for l,n in zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list(range(1,27)))
        }
        # print(tb)
        
        # traverse the string from right to left, update the answer
        ans = 0
        n = len(columnTitle)
        for i in range(n):
            ans += tb[columnTitle[n - 1 - i]] * (26 ** i)
        
        return ans
    
    