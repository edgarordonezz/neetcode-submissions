class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Order matters here
        res = []
        seen = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
            # if we've already tried nums continue
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                path.append(nums[i])
                backtrack(path)

                path.pop()
                seen.discard(nums[i])
        backtrack([])
        return res