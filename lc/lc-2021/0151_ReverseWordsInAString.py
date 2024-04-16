# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.split()))

class Solution:
    def reverse(self, s: list, start: int, end: int) -> str:
        while start<end:
            s[start],s[end] = s[end],s[start]
            start,end = start+1,end-1
        return s
    
    def reverseWords(self, s: str) -> str:
        N = len(s)
        
        if N<=1:
            return s
        else:
            # split the string into a list
            tmp = []
            left=0
            right=0
            while left<=right and right<N:
                if s[right]!=' ':
                    tmp.append(s[right])
                else:
                    if left<right:
                        tmp.append(' ')
                    left = right+1
                right += 1
            # clean the trailing space
            if tmp[-1]==' ':
                tmp.pop()
            # print(tmp)
            # reverse the whole list
            n = len(tmp)
            self.reverse(tmp,0,n-1)
            # print(tmp)
            # reverse each word
            left = 0
            right = 0
            while right<n:
                if tmp[right]==' ':
                    if left<right-1:
                        self.reverse(tmp,left,right-1)
                    left = right+1
                if right==n-1 and left<right:
                    self.reverse(tmp,left,right)
                right += 1
            # print(tmp)
            
            # reconstruct the string
            return ''.join(tmp)
            
                