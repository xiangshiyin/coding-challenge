class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # exceptions
        if len(s) == 1:
            return True

        # two pointers
        sp = 0
        tp = 0
        st = {}
        ts = {}
        N = len(s)

        while sp < N and tp < N:
            if s[sp] not in st:
                st[s[sp]] = t[tp]
            else:
                if st[s[sp]] != t[tp]:
                    return False
            if t[tp] not in ts:
                ts[t[tp]] = s[sp]
            else:
                if ts[t[tp]] != s[sp]:
                    return False

            # print(sp, tp, st, ts)
            sp += 1
            tp += 1
        # print(sp, tp, st, ts)

        return True
