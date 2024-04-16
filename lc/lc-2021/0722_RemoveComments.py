class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        flg = 0 # 1 means multi-line comments
        for ix,line in enumerate(source):
            n = len(line)
            
            # traverse the line, remove the commented part
            if ix == 0:
                cleaned = ''
            jx = 0
            while jx < n:
                if flg:
                    if line[jx:jx+2] == '*/':
                        flg = 0
                        if len(cleaned)>=2 and cleaned[-2:] == '/*':
                            cleaned = cleaned[:-2]
                        jx += 2
                    else:
                        jx += 1
                else:
                    if line[jx:jx+2] == '//':
                        break
                    elif line[jx:jx+2] == '/*':
                        cleaned += line[jx:jx+2]
                        jx += 2
                        flg = 1
                    else:
                        cleaned += line[jx]
                        jx += 1
                
            # append the cleaned code if not empty
            if len(cleaned) > 0:
                if flg == 0:
                    ans.append(cleaned)
                    cleaned = ''
        return ans

            
        
        