class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0->1->...->6
        # Assume repetitions dont count towards count
        # case: empty case
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in num_set:
                current_streak = 1
                while num + 1 in num_set:
                    num+=1
                    current_streak += 1
                if current_streak > longest:
                    longest = current_streak
        return longest
