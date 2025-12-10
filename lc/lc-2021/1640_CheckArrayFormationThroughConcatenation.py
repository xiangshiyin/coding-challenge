class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # build a lookup table based on arr
        helper = {}
        zero_counter = len(arr)
        for idx, num in enumerate(arr):
            helper[num] = idx

        # traverse the pieces
        outer = 0
        N = len(pieces)
        while outer < N:
            inner = 0
            idx_prev = -1
            n = len(pieces[outer])
            while inner < n:
                if pieces[outer][inner] not in helper:
                    return False
                else:
                    if idx_prev == -1:
                        idx_prev = helper[pieces[outer][inner]]
                    elif idx_prev >= 0 and helper[pieces[outer][inner]] - idx_prev == 1:
                        idx_prev = helper[pieces[outer][inner]]
                    else:
                        return False
                    zero_counter -= 1
                inner += 1
            outer += 1
        if zero_counter > 0:
            return False
        else:
            return True
