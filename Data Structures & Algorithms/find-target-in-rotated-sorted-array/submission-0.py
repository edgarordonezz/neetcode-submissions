class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # GOAL: Return the index of target or -1 if not present
        low = 0
        high = len(nums) - 1
        # while there are still elements in the array
        # I will be using binary search to find in O(log(n)) time
        # when middle number is smaller than our target
        # that means that the array was rotated and decreasing numbers
        # are now in higher indices than 
        while low <= high:
            # lets get our middle pointer
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            # if our left pointer is less than mid, left half is sorted
            if nums[low] <= nums[mid]:
                # now we check if target is in the range of the left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # if left is greater than target and right is less than target
            elif nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return -1