class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # exceptions
        if len(words)==1:
            return True
        
        # build the lookup table on lexicographical order
        tb = {letter:idx for idx,letter in enumerate(order)}
        
        # traverse the words and check the order
        l = 0
        r = 1
        while r<len(words):
            # locate the words
            lw = words[l]
            rw = words[r]
            # define inner pointers
            li = 0
            ri = 0
            while li<len(lw) and ri<len(rw):
                if tb[lw[li]]>tb[rw[ri]]:
                    return False  
                elif tb[lw[li]]<tb[rw[ri]]:
                    break
                else:
                    li += 1
                    ri += 1
            if li<len(lw) and ri==len(rw):
                return False
            # the two words follow the right order
            l = r
            r += 1
        return True
                    
            
            
        
        
        