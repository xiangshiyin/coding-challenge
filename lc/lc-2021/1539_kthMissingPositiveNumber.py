class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        prev = 0
        for idx in range(len(arr)):
            while prev < arr[idx] - 1:
                prev += 1
                counter += 1
                if counter == k:
                    return prev
            if idx < len(arr):
                prev = arr[idx]
        while counter < k:
            prev += 1
            counter += 1

        return prev
