class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        ix = 0
        while ix < n:
            ans.append(nums[ix])
            ans.append(nums[ix + n])
            ix += 1
        return ans
        