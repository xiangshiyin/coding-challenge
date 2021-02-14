class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # len1 = len(nums1) # the initial length of nums1
        # zero_counter = len1 - m
        # # step 1: add 0 placeholders if needed
        # if len1 < m + n:
        #     for i in range(len1, m+n):
        #         nums1.append(0)
        
        # step 2: fill in the elements to nums1
        right1 = m-1
        right2 = n-1
        right = m+n-1
        while (right1>=0)&(right2>=0):
            if nums1[right1]>nums2[right2]:
                nums1[right] = nums1[right1]
                right1 -= 1
            else:
                nums1[right] = nums2[right2]
                right2 -= 1
            right -= 1
        if right2>=0:
            while right2>=0:
                nums1[right] = nums2[right2]
                right2 -= 1
                right -= 1
            
def test(nums1, m, nums2, n):
    print(nums1)
    # len1 = len(nums1) # the initial length of nums1
    # zero_counter = len1 - m
    # # step 1: add 0 placeholders if needed
    # if len1 < m + n:
    #     for i in range(len1, m+n):
    #         nums1.append(0)
    
    # step 2: fill in the elements to nums1
    right1 = m-1
    right2 = n-1
    right = m+n-1
    while (right1>=0)&(right2>=0):
        if nums1[right1]>nums2[right2]:
            nums1[right] = nums1[right1]
            right1 -= 1
        else:
            nums1[right] = nums2[right2]
            right2 -= 1
        right -= 1
    if right2>=0:
        while right2>=0:
            nums1[right] = nums2[right2]
            right2 -= 1
            right -= 1
    print(nums1)

if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    test(nums1, m, nums2, n)