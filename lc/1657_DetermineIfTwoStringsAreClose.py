# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         '''
#         One line
#         '''
#         return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
    
    
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        general code
        '''
        
        # create table for character frequency
        f1 = {}
        for char in word1:
            if char not in f1:
                f1[char] = 1
            else:
                f1[char] += 1
        
        f2 = {}
        for char in word2:
            if char not in f2:
                f2[char] = 1
            else:
                f2[char] += 1
                
        # check the frequency of frequency values
        ff1 = {}
        for v in f1.values():
            if v not in ff1:
                ff1[v] = 1
            else:
                ff1[v] += 1
                
        ff2 = {}
        for v in f2.values():
            if v not in ff2:
                ff2[v] = 1
            else:
                ff2[v] += 1
        
        
        
        return set(word1) == set(word2) and ff1 == ff2
        
        
    