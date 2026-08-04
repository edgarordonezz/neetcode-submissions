class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2 # get the current middle element 
            # if target is greater than number at middle, that means target is hiding in the numbers too the right
            # so we increment our left pointer to check past that half
            if target > nums[middle]:
                l = middle + 1
            elif target < nums[middle]:
                r = middle - 1
            else: # else nums[middle] == target so we return the index
                return middle
        return -1