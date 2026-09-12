class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left = 1
        for i in range(n):
            res[i] = left
            # res = [1, 1, 2, 8]
            # for i = 0, res[i] = 1, left = 1
            # for i = 1, res[1] = 1, left = 2
            # for i = 2, res[2] = 2, left = 8
            # for i = 3, res[3] = 8, left = 48
            left = left * nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]
        
        return res