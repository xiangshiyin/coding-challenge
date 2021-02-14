class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # exception
        if digits=='':
            return []
        
        # traverse the digits
        tb = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        curr = []
        output = []
        def helper(pos, digits, tb, curr, output):
            if pos==len(digits):
                output.append(''.join(curr))
            elif pos<len(digits):
                digit = digits[pos] # find the digit
                for l in range(len(tb[digit])): # iterate through the values of a given digit
                    curr.append(tb[digit][l])
                    helper(pos+1, digits, tb, curr, output)
                    curr.pop()
        helper(0, digits, tb, curr, output)
        return output
    
            
            