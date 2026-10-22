class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            # add up left side
            current = max(nums[i], current + nums[i])
            # best holds the best we've seen
            best = max(best, current)
        return best