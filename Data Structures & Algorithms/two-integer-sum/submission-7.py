class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)): # starts at 0
            complement = target - nums[i] # find complement
            if complement in map: # if complement has been seen before
                return [map[complement], i] # return indices of complement and current number
            map[nums[i]] = i # store current number with its value
        