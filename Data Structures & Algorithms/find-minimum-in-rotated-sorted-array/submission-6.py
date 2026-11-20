class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # rotated case, search the right side
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
                