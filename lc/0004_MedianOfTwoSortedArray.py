
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # ascending by default
        # time complexity here should be O(m+n)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # #### extreme cases
        if len(nums1)==0:
            combo = nums2
        elif len(nums2)==0:
            combo = nums1
        elif nums1[-1]<=nums2[0]:
            combo = nums1 + nums2
        elif nums2[-1]<=nums1[0]:
            combo = nums2 + nums1
        else:
            #### regular cases
            low = nums1
            high = nums2
            low_p = high_p = 0
            combo = []
            #### set a step counter
            step = 0
            while (low_p<len(low))&(high_p<len(high)):
                if low[low_p]<=high[high_p]:
                    combo.append(low[low_p])
                    low_p += 1
                else:
                    combo.append(high[high_p])
                    #### switch array reference
                    temp = low
                    low = high
                    high = temp
                    #### swith array pointers
                    high_p += 1
                    temp_p = low_p
                    low_p = high_p
                    high_p = temp_p
                step += 1
            #### finish up populating combo
            if high_p<len(high):
                combo.extend(high[high_p:])
        result = combo[len(combo)//2] if len(combo)%2==1 else (combo[len(combo)//2-1] + combo[len(combo)//2])/2
        return(result)

    ## create function to get median of a given list
    def findMedianSortedArrays2(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        k = (l1+l2)//2
        if (l1+l2)%2==0:
            return((self.findKth(nums1,nums2,k) + self.findKth(nums1,nums2,k+1))/2)
        else:
            return(self.findKth(nums1,nums2,k+1))

    def findKth(self, nums1, nums2, k):
        l1 = len(nums1)
        l2 = len(nums2)
        ## change the order so that nums1 is always shorter than nums2
        if l1>l2:
            return(self.findKth(nums2, nums1, k))
        if l1==0:
            return(nums2[k-1])
        if k==1:
            return(min(nums1[0],nums2[0]))
        ## search through both arrays
        p1 = min(k//2,l1)
        p2 = k-p1
        if nums1[p1-1] <= nums2[p2-1]:
            return(self.findKth(nums1[p1:],nums2,p2))
        else:
            return(self.findKth(nums1,nums2[p2:],p1))


