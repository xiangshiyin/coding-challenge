class Solution:
    def reverse(self, s: list, start: int, end: int) -> None:
        while start < end:
            s[start],s[end] = s[end],s[start]
            start, end = start+1, end-1
        
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        if N>1:
            # reverse the whole list
            self.reverse(s, 0, N-1)
            # traverse the list, reverse the list section by section
            start = 0
            end = 0
            while end<N:
                if len(s[end].strip())==0:
                    if start<end-1:
                        self.reverse(s, start, end-1)
                    # update start and end
                    start = end + 1
                if end==N-1 and start<end:
                    self.reverse(s, start, end)
                end += 1
                