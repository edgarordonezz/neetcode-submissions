class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        # Condition: Numbers sum to target
        def backtrack(index, path, sum):
        # Base case: if sum == target, copy path to res
            if target == sum:
                res.append(path[:])
                return
            if sum > target:
                return
        
            # Constraint
            for i in range(index, len(nums)):
            # if i've tried this number and it isnt my first try, skip
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i, path, sum + nums[i])
                path.pop()


        backtrack(0, [], 0)
        return res


                