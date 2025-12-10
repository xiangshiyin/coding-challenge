class Solution:
    def swap(self, nums: list, first: int, output: list) -> None:
        N = len(nums)
        if first == N:
            output.append(nums[:])
        for i in range(first, N):
            if nums[first] != nums[i]:
                nums[first], nums[i] = nums[i], nums[first]
            self.swap(nums, first + 1, output)
            if nums[first] != nums[i]:
                nums[first], nums[i] = nums[i], nums[first]

    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.swap(nums, 0, output)
        return output
