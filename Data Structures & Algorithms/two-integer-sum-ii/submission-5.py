class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # when target = 3, 1 + 2 = 3, target = s[l] + s[r]
        # if s[l] = s[r] - target return
        res = []
        l = 0
        r = len(numbers) - 1
        while l < r:
            # if sum is too small, increment l
            candidate = numbers[l] + numbers[r]
            if candidate < target:
                l += 1
            elif candidate > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return res