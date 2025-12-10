# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # get frequency hash table
#         freq = {}
#         for num in nums:
#             if num not in freq:
#                 freq[num] = 1
#             else:
#                 freq[num] += 1


#         if len(freq) <= k:
#             return list(freq.keys())

#         print(freq)
#         # find the top K frequent numbers
#         from heapq import heappush, heappushpop

#         hp = []
#         for num in freq:
#             if len(hp) < k:
#                 heappush(hp, (freq[num], num))
#             else:
#                 heappushpop(hp, (freq[num], num))

#         return [v[1] for v in hp]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         '''
#         O(n) solution
#         '''
#         N = len(nums)
#         bucket = [[] for i in range(N+1)]

#         from collections import Counter
#         from itertools import chain
#         count = Counter(nums)

#         for num,freq in count.items():
#             bucket[freq].append(num)


#         concat = list(chain(*bucket))
#         return concat[::-1][:k]


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         '''
#         with built-in function in heapq
#         '''
#         N = len(nums)

#         from collections import Counter
#         from heapq import nlargest
#         count = Counter(nums)
#         return nlargest(k, count.keys(), key = lambda x: count[x])


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        With quick select
        """
        from collections import Counter

        count = Counter(nums)
        unique = list(count.keys())
        print(unique)

        def partition(left, right, pivot_index):
            pivot_freq = count[unique[pivot_index]]
            # step 1: move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            # step 2: move all less freq elements to the left
            curr = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[curr], unique[i] = unique[i], unique[curr]
                    curr += 1
            # step 3: move pivot to final place
            unique[curr], unique[right] = unique[right], unique[curr]

            return curr

        def quickselect(left, right, k_smallest):
            if left == right:
                return

            import random

            pivot_index = random.randint(left, right)

            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)

        quickselect(0, n - 1, n - k)  # n - k smallest

        return unique[n - k :]
