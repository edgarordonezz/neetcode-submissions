class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            val = abs(nums[i]) # pointer
            if nums[val] < 0:
                return abs(val) # return pointer
            nums[val] *= -1