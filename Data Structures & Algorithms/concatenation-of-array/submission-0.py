class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cpy = nums.copy()
        res = [0] * len(nums) * 2
        for i in range(len(nums)):
            res[i] = nums[i]
        res[len(nums): len(res) + 1] = cpy
        
        return res