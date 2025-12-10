class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        Two pointer, run fast but takes too much memory??
        """
        # exceptions
        if len(s) - len(t) > 1:
            return False
        elif s == t:
            return False

        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if len(s) == len(t):
                    if s[(i + 1) :] == t[(j + 1) :]:
                        return True
                    else:
                        return False
                elif len(s) > len(t):
                    if s[(i + 1) :] == t[j:]:
                        return True
                    else:
                        return False
                else:
                    if s[i:] == t[(j + 1) :]:
                        return True
                    else:
                        return False
            i += 1
            j += 1

        if len(s[i:]) + len(t[j:]) == 1:
            return True
        else:
            return False
