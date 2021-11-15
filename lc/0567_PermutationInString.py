class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        use hashmap to record frequencies of letters
        '''
        # exception
        if len(s2) < len(s1):
            return False
        
        from collections import defaultdict
        # get the map for s1
        mp1 = defaultdict(int)
        for ch in s1:
            mp1[ch] += 1
        
        mp2 = defaultdict(int)
        # traverse s2
        for i in range(len(s2)):
            if i == 0:
                for ch in s2[:len(s1)]:
                    mp2[ch] += 1
            elif i + len(s1) <= len(s2):
                mp2[s2[i + len(s1) - 1]] += 1
                if mp2[s2[i - 1]] == 1:
                    mp2.pop(s2[i - 1])
                else:
                    mp2[s2[i - 1]] -= 1
            else:
                return False
            
            if mp2 == mp1:
                return True
            
        
        
