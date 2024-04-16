class Solution:
    def fib(self, n: int) -> int:
        for i in range(n + 1):
            if i == 0:
                prev = 0
                curr = 0
            elif i == 1:
                curr = 1
            else:
                tmp = prev + curr
                prev = curr
                curr = tmp
        return curr
              
              