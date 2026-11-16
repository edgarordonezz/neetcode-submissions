class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        mp = {0: 1}
        left = [0] * len(nums)
        left[0] = nums[0]
        # 1, 2, 3
        # left = [0,0,0]
        # left[0] = 0(left[0]) + 1(nums[0]) = 1
        # left[1] = 1(left[0])+ 2(nums[1]) = 3
        # and then we reuse left[1] to compute left[2]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] + nums[i]
        # now left = [1, 3, 6], k = 3
        # now we hashmap and check for left[0], does 3 = 1 + x, does x exist
        # x would be 2, it does exist in nums
        for curr in left:
            count += mp.get(curr - k, 0)
            mp[curr] = mp.get(curr, 0) + 1
            
        return count