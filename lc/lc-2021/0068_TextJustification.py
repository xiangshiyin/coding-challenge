class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        # create length lookup table
        ls = [len(w) for w in words]
        
        ix = 0
        ans = []
        while ix < n:
            q = [words[ix]]
            curr_len = ls[ix]
            ix += 1
            while ix < n and curr_len + ls[ix] + 1 <= maxWidth:
                q.append(words[ix])
                curr_len += ls[ix] + 1
                ix += 1
            # format the string
            num_spaces = maxWidth - sum([len(w) for w in q])
            if len(q) > 1 and ix < n:
                space_per_slot = num_spaces // (len(q) - 1)
                extras = num_spaces % (len(q) - 1)
                tmp = q[0]
                for i in range(1,len(q)):
                    if i <= extras and extras:
                        tmp += ' ' * (space_per_slot + 1) + q[i]
                    else:
                        tmp += ' ' * space_per_slot + q[i]
                ans.append(tmp)
            else:
                tmp = ' '.join(q) + ' ' * (num_spaces - len(q) + 1)
                ans.append(tmp)
            # print(q, num_spaces, len(q) - 1, space_per_slot, extras)
        
        return ans
    
    