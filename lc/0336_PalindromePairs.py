# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         '''
#         O(n2) solution, exceeded time limit
#         '''
#         N = len(words)
#         # exception
#         if N == 1:
#             return []
        
#         # define a function to check if the given pair makes a palindrome
#         def check(s1, s2):
#             s = s1 + s2
#             p1 = 0
#             p2 = len(s)-1
#             while p1 < p2 and p2 >= 0 and s[p1] == s[p2]:
#                 p1 += 1
#                 p2 -= 1
#             if p1 >= p2:
#                 return True
#             else:
#                 return False
        
#         # traverse the words
#         output = []
        
#         for i in range(N):
#             for j in range(N):
#                 if i != j and check(words[i], words[j]): # palindrome pair
#                     output.append([i,j])
                    
#         return output


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        O(n2) solution
        '''
        N = len(words)
        # exception
        if N == 1:
            return []
        
        # create a lookup table for all words' address
        tb = {w:i for i,w in enumerate(words)}
        # print(tb)
        
        output = []
        for i,w in enumerate(words):
            for j in range(len(w)+1):
                left, right = w[:j], w[j:]
                if j != 0 and left[::-1] == left and right[::-1] in tb and tb[right[::-1]] != i:
                    output.append([tb[right[::-1]], i])
                if right[::-1] == right and left[::-1] in tb and tb[left[::-1]] != i:
                    output.append([i, tb[left[::-1]]])
        return output
                    
                    
                
    
    