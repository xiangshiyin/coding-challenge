class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a lookup table based on nums1
        helper = {}
        for num in nums1:
            if num not in helper:
                helper[num] = 1
            else:
                helper[num] += 1
        
        # traverse nums2, generate output
        output = []
        for num in nums2:
            if num in helper and helper[num] > 0:
                output.append(num)
                helper[num] -= 1
        return output
