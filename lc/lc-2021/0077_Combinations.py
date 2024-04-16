class Solution:
    def helper(self, n: int, k: int, first: int, curr: list, output: list) -> None:
        if len(curr)==k:
            output.append(curr[:])
        else:
            for i in range(first, n+1):
                curr.append(i)
                self.helper(n, k, i+1, curr, output)
                curr.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        output = []
        self.helper(n, k, 1, curr, output)
        return output
        
        