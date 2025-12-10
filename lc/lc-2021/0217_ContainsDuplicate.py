class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # exceptions
        if nums is None:
            return False
        N = len(nums)
        if N <= 1:
            return False

        # traverse the list
        tb = set()
        for num in nums:
            if num not in tb:
                tb.add(num)
            else:
                return True
