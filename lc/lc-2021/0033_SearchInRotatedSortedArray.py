class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            # print(l, m, r, nums[l] > nums[m], target < nums[m])

            if nums[m] == target:
                return m
            elif l == r and nums[m] != target:
                return -1

            # determine the scenarios
            if nums[l] > nums[m]:
                # scenario 1
                if target < nums[m]:
                    r = m - 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                # scenario 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
