class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = []
        while l < r:
            cand = numbers[l] + numbers[r]
            if target == cand:
                res.append(l+1)
                res.append(r+1)
                break
            # if cand < target that means we increment left
            if cand < target:
                l += 1
            if cand > target:
                r -= 1
        return res