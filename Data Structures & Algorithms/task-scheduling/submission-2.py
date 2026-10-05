class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the frequency of letters
        freq = [0] * 26
        maxCount = 0
        tied = 0
        for task in tasks:
            idx = ord(task) - ord('A')
            freq[idx] += 1
            maxCount = max(maxCount, freq[idx])

        for count in freq:
            if count == maxCount:
                tied += 1
        fullChunks = maxCount - 1
        width = n + 1
        res = fullChunks * width + tied
        return res if len(tasks) < res else len(tasks)