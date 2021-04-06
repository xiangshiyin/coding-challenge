class Solution:
    def originalDigits(self, s: str) -> str:
        tb = {
            'zero':'0',
            'one':'1',
            'two':'2',
            'three':'3',
            'four':'4',
            'five':'5',
            'six':'6',
            'seven':'7',
            'eight':'8',
            'nine':'9'
        }
        
        ls  = ['z','u','g','w','x','f','v','o','h','i']
        ws = ['zero','four','eight','two','six','five','seven','one','three','nine']
        
        from collections import Counter
        freq = Counter(s)
        counts = [0 for i in range(10)]
        
        for ix,l in enumerate(ls):
            counts[ix] = freq[l]
            # update frequency table
            tmp = Counter(ws[ix])
            iters = 0
            while iters < counts[ix]:
                freq = freq - tmp
                iters += 1
        # print(counts)
        
        # generate the output
        ans = []
        for ix,c in enumerate(counts):
            if c > 0:
                ans.append(tb[ws[ix]] * c)
        # print(ans)
        
        return ''.join(sorted(ans))

    
        
        