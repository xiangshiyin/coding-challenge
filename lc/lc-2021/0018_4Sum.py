class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        
        # sort nums
        nums.sort()
        
        cd = {}
        # create hash table to record c + d:
        for i in range(N-1):
            for j in range(i+1, N):
                if target - 1 * (nums[i] + nums[j]) not in cd:
                    cd[target - 1 * (nums[i] + nums[j])] = [[i,j]]
                else:
                    cd[target - 1 * (nums[i] + nums[j])].append([i,j])

        # check all combinations of a + b:
        output = []
        visited = set()
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] in cd:
                    for k,l in cd[nums[i] + nums[j]]:
                        if k > j and (nums[i],nums[j],nums[k],nums[l]) not in visited:
                            output.append([nums[i],nums[j],nums[k],nums[l]])
                            visited.add((nums[i],nums[j],nums[k],nums[l]))
                            
        return output
                    