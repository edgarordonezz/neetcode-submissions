class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            # if cand is too big decrement r pointer
            # if cand is too small, increment r pointer
            cand = numbers[l] + numbers[r]
            if cand < target and numbers[l] != numbers[r]:
                l += 1
            elif cand > target and numbers[l] != numbers[r]:
                r -= 1
            else:
                return [l + 1, r + 1]
            