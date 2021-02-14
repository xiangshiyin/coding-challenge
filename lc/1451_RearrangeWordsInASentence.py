class Solution:
    def arrangeWords(self, text: str) -> str:
        N = len(text)
        
        if N<=1:
            return text
        else:
            tmp = sorted(text.lower().split(), key=len)
            # fix the initial letter
            tmp[0] = tmp[0][0].upper()+tmp[0][1:]
            return ' '.join(tmp)
            