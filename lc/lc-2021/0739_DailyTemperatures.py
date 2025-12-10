# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         '''
#         Use a stack to store smaller numbers, use a hashtable to store distance
#         '''
#         n = len(T)
#         # exception
#         if n == 1:
#             return 0

#         # traverse the list
#         idx = 0
#         tb = {}
#         stack = []

#         while idx < n:
#             if idx == n - 1:
#                 tb[idx] = 0
#                 break

#             if T[idx] >= T[idx + 1]:
#                 stack.append(idx)
#             else: # found a warmer day
#                 tb[idx] = 1 # +1 step
#                 while len(stack) > 0 and T[stack[-1]] < T[idx + 1]:
#                     tb[stack[-1]] = idx + 1 - stack[-1]
#                     stack.pop()
#             idx += 1

#         while stack:
#             tb[stack[-1]] = 0
#             stack.pop()

#         return [tb[i] for i in range(n)]


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Similar solution with stack, dropped hash table, memory usage decreased dramatically
        """
        n = len(T)
        # exception
        if n == 1:
            return 0

        # traverse the list
        idx = 0
        result = [0 for i in range(n)]
        stack = []

        while idx < n:
            if idx == n - 1:
                result[idx] = 0
                break

            if T[idx] >= T[idx + 1]:
                stack.append(idx)
            else:  # found a warmer day
                result[idx] = 1  # +1 step
                while len(stack) > 0 and T[stack[-1]] < T[idx + 1]:
                    result[stack[-1]] = idx + 1 - stack[-1]
                    stack.pop()
            idx += 1

        while stack:
            result[stack[-1]] = 0
            stack.pop()

        return result
