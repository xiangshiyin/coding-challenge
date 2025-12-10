## implementing dp algorithm
## on 8/7/2018


#### DP solution
def fib(n, memo):
    # memo = [None]*n
    if memo[n - 1] != None:
        return memo[n - 1]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n - 1] = result
    return result


#### Bottom-up solution
def fib2(n):
    memo = [1, 1]
    for i in range(3, n + 1):
        memo.append(memo[i - 2] + memo[i - 3])
    return memo[n - 1]
