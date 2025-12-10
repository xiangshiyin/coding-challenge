class NumArray:
    def __init__(self, nums: List[int]):
        self.presums = [0]
        for i in range(1, len(nums) + 1):
            self.presums.append(self.presums[-1] + nums[i - 1])

    def sumRange(self, left: int, right: int) -> int:
        return self.presums[right + 1] - self.presums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
