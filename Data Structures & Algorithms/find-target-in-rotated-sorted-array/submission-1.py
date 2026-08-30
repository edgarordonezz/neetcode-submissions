class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            # this means that array was rotated, this means right side is incrementing
            # and left side is decrementing
            if target == nums[middle]:
                return middle
            if nums[middle] > nums[right]:
                # if middle is greater than target and target is greater than right
                if nums[left] <= target <= nums[middle]:
                    # target IS in the sorted left portion
                    # so we would decrement right
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    # target IS in the sorted right portion
                    left = middle + 1
                else:
                    right = middle - 1
        return - 1