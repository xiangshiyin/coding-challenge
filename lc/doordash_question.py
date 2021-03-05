class Solution:
    def longestSubstring(self, input):
        N = len(input)
        # create a hashtable for position of p string
        p = {}
        xy = [0,0] # start and end of the substring
        xy_curr = [0,0]

        for idx in range(0,N-1,2):
            if input[idx]=='P': # P*
                if input[idx+1] not in p:
                    p[input[idx+1]] = [idx] # the index of P
                else:
                    p[input[idx+1]].append(idx) # the index of P
            else: # Q*
                if input[idx+1] not in p:
                    # clear out p
                    p = {}
                    xy_curr = []
                elif p[input[idx+1]]==[]:
                    p = {}
                    xy_curr = []
                else: # found a match
                    if xy_curr==[]:
                        xy_curr = [p[input[idx+1]][-1],idx+1]
                    elif p[input[idx+1]][-1]<=xy_curr[1]+1: # right after the previous pair found
                        xy_curr[0],xy_curr[1] = min(xy_curr[0],p[input[idx+1]][-1]),max(xy_curr[1],idx+1)
                    elif (idx+1)-p[input[idx+1]][-1]>=xy_curr[1]-xy_curr[0]:
                        xy_curr = [p[input[idx+1]][-1], idx+1]      
                    p[input[idx+1]].pop()

                    # compare with xy
                    if xy_curr[0]<=xy[1]:
                        xy[0],xy[1] = min(xy[0],xy_curr[0]),max(xy[1],xy_curr[1])
                    elif xy_curr[1]-xy_curr[0]>=xy[1]-xy[0]:
                        xy = xy_curr
            print(p,xy)
        if xy[1]-xy[0]>3:
            print(input[xy[0]:xy[1]+1])



if __name__ == "__main__":
    # Solution().longestSubstring('P4P1D1P2D2')
    Solution().longestSubstring('P4P5P1D1P2D2D3P4D4P5P6D5D6P7D7')