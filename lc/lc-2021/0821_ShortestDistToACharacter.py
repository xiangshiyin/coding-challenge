# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         # exception
#         if len(s) == 1:
#             return 0

#         # 1st pass, find all locations of character c
#         idx = [i for i,char in enumerate(s) if char == c]

#         # 2nd pass, traverse the string, find the shortest distance
#         output = []
#         left = 0
#         right = 0

#         for i in range(len(s)):
#             if right < len(idx):
#                 if i <= idx[right]:
#                     output.append(min(abs(i - idx[left]), abs(idx[right] - i)))
#                 else:
#                     left = right
#                     right += 1
#                     if right < len(idx):
#                         output.append(min(abs(i - idx[left]), abs(idx[right] - i)))
#                     else:
#                         output.append(i - idx[left])
#             else:
#                 output.append(i - idx[left])

#         return output


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        2 pass solution
        """
        N = len(s)
        output = []
        pos = -N
        # 1st pass, calculate the distance to characters on the left
        for i in range(N):
            if s[i] == c:
                pos = i
            output.append(i - pos)

        # 2nd pass, calculate the distance to characters on the right, update output
        for i in range(N - 1, -1, -1):
            if s[i] == c:
                pos = i
            if pos > i:
                output[i] = min(output[i], pos - i)
        return output
