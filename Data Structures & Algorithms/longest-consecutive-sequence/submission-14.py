class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set()
        # add numbers to num to see if a consecutive number exists
        for num in nums:
            freq.add(num)
        longest = 0
        for num in freq:
            # only start if number begins a sequence
            if num - 1 not in freq:
                count = 1
                consecutive = num + 1
                while consecutive in freq:
                    count += 1
                    consecutive += 1
                longest = max(longest, count)
            else:
                continue
        return longest