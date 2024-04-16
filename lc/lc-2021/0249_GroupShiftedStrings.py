# class Solution:
#     def groupStrings(self, strings: List[str]) -> List[List[str]]:
#         # define a utility function to extract the string pattern
#         # 25 = -1
#         # 24 = -2
        
#         def getPattern(string):
#             pattern = []
#             for i in range(len(string)):
#                 if i == 0:
#                     pattern.append(i)
#                 else:
#                     diff = ord(string[i]) - ord(string[i - 1])
#                     if diff >= 0:
#                         pattern.append(diff)
#                     else:
#                         pattern.append(26 + diff)
#             return tuple(pattern)
        
#         # traverse the list and generate output
#         patterns = {}
#         for string in strings:
#             pattern = getPattern(string)
#             if pattern not in patterns:
#                 patterns[pattern] = [string]
#             else:
#                 patterns[pattern].append(string)
        
#         return [patterns[key] for key in patterns]
        
        
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        patterns = {}
        
        for string in strings:
            pattern = []
            for i in range(len(string)):
                if i == 0:
                    pattern.append(0)
                else:
                    pattern.append((26 + ord(string[i]) - ord(string[i - 1])) % 26)
            
            pattern = tuple(pattern)
            if pattern not in patterns:
                patterns[pattern] = [string]
            else:
                patterns[pattern].append(string)
        
        return [patterns[key] for key in patterns]        
                
                
        
        
        