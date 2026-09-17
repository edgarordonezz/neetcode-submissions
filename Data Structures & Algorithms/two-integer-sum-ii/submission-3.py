class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = []
        while l < r:
            cand = numbers[l] + numbers[r]
            # if cand < target that means we increment left
            if cand < target:
                l += 1
            elif cand > target:
                r -= 1
            else:
                res = [l+1, r+1]
                break
        return res