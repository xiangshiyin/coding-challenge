class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # create a hash table for 180 degree rotation mapping
        helper = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        # flip the given string
        num2 = ""
        n = len(num)
        i = n - 1
        while i >= 0:
            if num[i] in helper:
                num2 += helper[num[i]]
            else:
                return False
            i -= 1
        return num2 == num
