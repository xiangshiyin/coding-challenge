# class Solution:
#     def minInsertions(self, s: str) -> int:
#         '''
#         O(n) solution with stack
#         '''
#         N = len(s)

#         # traverse the string
#         toadd = 0
#         stack = []
#         i = 0
#         while i<N:
#             if s[i]=='(':
#                 stack.append(s[i])
#                 i += 1
#             else:
#                 if s[i:i+2]=='))':
#                     if len(stack)>0:
#                         stack.pop()
#                     else:
#                         toadd += 1
#                     i += 2
#                 else:
#                     if len(stack)>0:
#                         stack.pop()
#                         toadd += 1
#                     else:
#                         toadd += 2
#                     i += 1
#         # check the length of stack
#         if len(stack)>0:
#             toadd += len(stack)*2

#         return toadd


class Solution:
    def minInsertions(self, s: str) -> int:
        """
        O(n) solution without stack
        """
        N = len(s)
        # traverse the string
        lcounter = 0
        toadd = 0

        i = 0
        while i < N:
            if s[i] == "(":
                lcounter += 1
                i += 1
            else:
                if s[i : i + 2] == "))":
                    if lcounter > 0:
                        lcounter -= 1
                        i += 2
                    else:
                        toadd += 1
                        i += 2
                else:
                    if lcounter > 0:
                        toadd += 1
                        lcounter -= 1
                        i += 1
                    else:
                        toadd += 2
                        i += 1
        return toadd + lcounter * 2
