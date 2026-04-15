class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in my_map:
                return [my_map[compliment], i]
            my_map[nums[i]] = i
        