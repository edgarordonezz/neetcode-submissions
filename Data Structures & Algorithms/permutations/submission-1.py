class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # since unique, we can use a set
        used = set()
        path = []
        def backtrack(count):
            
            if len(nums) == count:
                res.append(path[:])
                return
            for num in nums:
                if num in used:
                    continue
                else:
                    used.add(num)
                    path.append(num)
                    backtrack(count + 1)
                    path.pop()
                    used.remove(num)
                
        backtrack(0)
        return res

            
