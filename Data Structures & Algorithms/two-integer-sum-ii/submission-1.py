class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        # Since array is already sorted, we will use two pointers
        # Since we need to find target we just add numbers at the indices
        # if sum is too small we just increment smaller pointer
        # if sum is too big we just decrement bigger pointer
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            complement = numbers[left] + numbers[right]
            if complement < target:
                left+=1
            elif complement > target:
                right-=1
            else:
                return [left+1,right+1]