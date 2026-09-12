class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for index 0 we need to just know prefix = 0
        # postfix = 2 * 4 * 6
        # total = 48
        # for index 1 prefix = 1, postfix = 24
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res