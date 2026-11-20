class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        n = len(nums)
        res = 0
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
            if mp[num] > n // 2:
                res = num
        return res