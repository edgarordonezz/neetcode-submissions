class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        result = []

        for i in range(len(nums)):
            # if we sort and all numbers are positive we cannot find 0
            if i > 0 and nums[i] > 0:
                break

            # skip duplicates at index i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # left pointer starts after nums[i]
            left = i + 1 
            # right pointer at nums[]
            right = len(nums) - 1 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # if the number is too small, increment left pointer
                if total < 0:
                    left += 1
                # if number is too big, decrement right pointer
                elif total > 0:
                    right -= 1
                else:
                # if number == 0, create a list of the numbers and fix increment/decrement pointers
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result


