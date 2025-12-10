class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        the array nums is pre-sorted
        """
        N = len(nums)
        left = 0
        right = N - 1
        seen = set()
        output = []

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                if nums[left] not in seen:
                    output.append([nums[left], nums[right], -1 * target])
                    seen.add(nums[left])
                right -= 1
        return output

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N < 3:
            return []
        else:
            # sort the list
            nums2 = sorted(nums)
            # prepare for the searching
            seen = set()
            idx = N - 1
            output = []

            while idx >= 0:
                target = nums2[-1]  # cache the value
                nums2.pop()  # remove the largest
                if target not in seen:  # do the search
                    seen.add(target)
                    output.extend(self.twoSum(nums2, -1 * target))
                idx -= 1
            return output
