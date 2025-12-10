class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        # get the total sum
        total = sum(nums)
        if total < x:
            return -1
        elif total == x:
            return N
        # print(total)

        # when total > x:
        left = 0
        right = 0
        max_len = 0
        curr_sum = nums[0]

        while left <= right and right < N:
            if curr_sum <= total - x:
                if curr_sum == total - x:
                    max_len = max(max_len, right - left + 1)
                right += 1
                if right < N:
                    curr_sum += nums[right]
            else:
                curr_sum -= nums[left]
                left += 1
                if left > right:
                    right = left
                    curr_sum += nums[right]
            # print(max_len, curr_sum, left, right)
        if max_len == 0:
            return -1
        else:
            return len(nums) - max_len
