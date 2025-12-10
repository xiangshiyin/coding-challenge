class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [""]
        for char in S:
            if char.isalpha():
                result = [r + ch for r in result for ch in [char.lower(), char.upper()]]
            else:
                result = [r + char for r in result]
        return result


# solution as of 11/16/2021
# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         def helper(s, target, output):
#             n = len(s)
#             if target == n:
#                 output.append(''.join(s))
#             else:
#                 if s[target].isalpha():
#                     for candidate in (s[target].lower(), s[target].upper()):
#                         cache = s[target]
#                         if candidate != cache:
#                             s[target] = candidate

#                         helper(s, target+1, output)

#                         if candidate != cache:
#                             s[target] = cache
#                 else:
#                     helper(s, target+1, output)

#         output = []
#         s2 = list(s)
#         helper(s2, 0, output)

#         return output
