# class FreqStack:
#     '''
#     heap + hash table
#     '''
#     from collections import defaultdict
#     from heapq import heappush, heappop

#     def __init__(self):
#         self.counter = 0
#         self.freq_dict = defaultdict(int)
#         self.q = []


#     def push(self, x: int) -> None:
#         self.freq_dict[x] += 1
#         self.counter += 1
#         heappush(self.q, (-self.freq_dict[x], -self.counter, x))
#         # print(self.q)


#     def pop(self) -> int:
#         res = heappop(self.q)
#         self.freq_dict[res[2]] -= 1
#         return res[2]


class FreqStack:
    """
    hash table
    """

    from collections import defaultdict

    def __init__(self):
        self.freq_dict = defaultdict(int)
        self.freq_group = defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.freq_dict[x] += 1
        self.maxfreq = max(self.maxfreq, self.freq_dict[x])
        self.freq_group[self.freq_dict[x]].append(x)
        # print(self.freq_group)

    def pop(self) -> int:
        res = self.freq_group[self.maxfreq].pop()
        self.freq_dict[res] -= 1
        if not self.freq_group[self.maxfreq]:
            self.maxfreq -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
