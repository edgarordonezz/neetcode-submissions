class Solution:
    def findMin(self, nums: List[int]) -> int:
        # so we know it's sorted, we can use binary search to find the smallest value
        # if middle of array is smaller than left side, that means that the list is rotated
        # if left side is greater than, we have to check the right side, so we move left to middle + 1
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]: # if middle is greater than right, list is rotated so we check the right side
                left = middle + 1
            else:
                right = middle
        # will end once left <= right so we return left
        return nums[left]
