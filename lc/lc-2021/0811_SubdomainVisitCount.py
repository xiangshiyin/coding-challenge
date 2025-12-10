class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        use hash table to store the frequencies
        """
        from collections import defaultdict

        tb = defaultdict(int)

        for cpdomain in cpdomains:
            freq, domain = cpdomain.split()
            freq = int(freq)

            # traverse the domain from right to left
            n = len(domain)
            i = n - 1
            while i >= 0:
                if domain[i] == ".":
                    tb[domain[i + 1 :]] += freq
                i -= 1
            tb[domain] += freq

        return [f"{v} {k}" for k, v in tb.items()]
