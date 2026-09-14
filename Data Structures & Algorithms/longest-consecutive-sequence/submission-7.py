class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        unique = set(nums)
        for num in unique:
            start = num - 1
            if start not in unique:
                curr = num
                length = 1 # start itself counts as 1
                while (curr + 1) in unique:
                    curr += 1
                    length += 1
                count = max(count, length)
        return count
        

        # [2, 1, 3]
        # if 1 is not in unique:
        # this fails so we start the count at 1 by setting new_start = start