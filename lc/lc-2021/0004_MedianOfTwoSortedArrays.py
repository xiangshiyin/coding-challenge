# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         '''
#         O(n) solution
#         '''
#         n1 = len(nums1)
#         n2 = len(nums2)
#         m = (n1 + n2) // 2

#         # special cases
#         if not n1 and not n2:
#             return None

#         #
#         nums = []
#         ix = 0
#         jx = 0
#         while ix < n1 and jx < n2:
#             if nums1[ix] <= nums2[jx]:
#                 nums.append(nums1[ix])
#                 ix += 1
#             else:
#                 nums.append(nums2[jx])
#                 jx += 1


#         while ix < n1:
#             if len(nums) - n2 == ix + 1:
#                 ix += 1
#             if ix < n1:
#                 nums.append(nums1[ix])
#                 ix += 1
#         while jx < n2:
#             if len(nums) - n1 == jx + 1:
#                 jx += 1
#             if jx < n2:
#                 nums.append(nums2[jx])
#                 jx += 1

#         if (n1 + n2) % 2 == 1:
#             return nums[m]
#         else:
#             return (nums[m] + nums[m - 1])  / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        O(log(n)) solution
        """
        n1 = len(nums1)
        n2 = len(nums2)
        k = (n1 + n2) // 2  # median

        if not nums1 and not nums2:
            return None
        elif not nums1:
            if n2 % 2 == 1:
                return nums2[k]
            else:
                return (nums2[k - 1] + nums2[k]) / 2
        elif not nums2:
            if n1 % 2 == 1:
                return nums1[k]
            else:
                return (nums1[k - 1] + nums1[k]) / 2

        if n2 < n1:
            return self.findMedianSortedArrays(nums2, nums1)

        l = 0
        r = n1

        while l < r:
            m1 = (l + r) // 2
            m2 = k - m1
            # print(l,r,m1,m2)
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1

        # recalculate m1 and m2
        m1 = (l + r) // 2
        m2 = k - m1

        # print(f'l={l}, r={r}, m1={m1}, m2={m2}, n1={n1}, n2={n2}')

        if (n1 + n2) % 2 == 1:
            if m1 == n1:
                return nums2[m2] if m2 >= 0 else nums1[m1 - 1]
            elif m2 == n2:
                return nums1[m1] if m1 >= 0 else nums2[m2 - 1]
            else:
                return min(nums1[m1], nums2[m2])
        else:
            if m1 == 0:
                return (
                    (nums2[m2 - 1] + min(nums1[m1], nums2[m2])) / 2
                    if m2 < n2
                    else (nums2[m2 - 1] + nums1[m1]) / 2
                )
            elif m1 == n1:
                return (
                    (max(nums1[m1 - 1], nums2[m2 - 1]) + nums2[m2]) / 2
                    if m2 >= 1
                    else (nums1[m1 - 1] + nums2[m2]) / 2
                )
            elif m2 == 0:
                return (
                    (nums1[m1 - 1] + min(nums1[m1], nums2[m2])) / 2
                    if m1 < n1
                    else (nums1[m1 - 1] + nums2[m2]) / 2
                )
            elif m2 == n2:
                return (
                    (max(nums1[m1 - 1], nums2[m2 - 1]) + nums1[m1]) / 2
                    if m1 >= 1
                    else (nums2[m2 - 1] + nums1[m1]) / 2
                )
            else:
                return (
                    max(nums1[m1 - 1], nums2[m2 - 1]) + min(nums1[m1], nums2[m2])
                ) / 2
