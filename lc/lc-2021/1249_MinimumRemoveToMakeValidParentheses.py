class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # step 1: 1st pass, traverse the string from left to right
        lcounter = 0
        rcounter = 0
        marker = 0
        toremove1 = []

        for i, char in enumerate(s):
            if char == "(":
                lcounter += 1
            elif char == ")":
                rcounter += 1

            if rcounter > lcounter:
                toremove1.append(i)
                lcounter = 0
                rcounter = 0
                marker = i + 1

        # print(lcounter, rcounter, toremove1)
        # step 2:
        toremove2 = []
        if lcounter > rcounter:
            # 2nd pass, traverse the string from right to left
            lcounter = 0
            rcounter = 0
            for j in range(len(s) - 1, marker - 1, -1):
                if s[j] == "(":
                    lcounter += 1
                elif s[j] == ")":
                    rcounter += 1

                if rcounter < lcounter:
                    toremove2.append(j)
                    lcounter = 0
                    rcounter = 0
        # print(lcounter, rcounter, toremove1, toremove2)
        # step 3: remove the redundant parentheses
        s2 = [char for char in s]
        # print(s2)
        # print(len(s2))
        # print(toremove1)
        # print(toremove2)

        if toremove2 != []:
            for idx in toremove2:
                s2.pop(idx)

        if toremove1 != []:
            toremove1.reverse()
            for idx in toremove1:
                s2.pop(idx)

        return "".join(s2)
