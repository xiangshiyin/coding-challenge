class Solution:
    def simplifyPath(self, path: str) -> str:
        # step 1: clean the trailing '/' and leading '/'
        path = path.strip('/')
        
        # step 2: break the string into a list
        dirs = path.split('/')
        path2 = ''
        N = len(dirs)
        
        i = N - 1
        delta = 0
        while i >=0:
            l = len(dirs[i])
            if l > 0:
                if dirs[i] == '.' * l:
                    if l <= 2:
                        delta = delta + l - 1
                    else:
                        if delta == 0:
                            path2 = ('/' + dirs[i]) + path2
                        else:
                            delta -= 1
                else:
                    if delta == 0:
                        path2 = ('/' + dirs[i]) + path2
                    else:
                        delta -= 1
                        
            i -= 1
        
        return path2 if path2 != '' else '/'
                