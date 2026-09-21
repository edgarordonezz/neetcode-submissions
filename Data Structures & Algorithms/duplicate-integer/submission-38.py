class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for num in nums:
            if num in mp:
                return True
            mp[num] = mp.get(num, 0) + 1
        return False