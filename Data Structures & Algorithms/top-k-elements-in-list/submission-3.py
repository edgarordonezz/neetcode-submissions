class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # definitely need a map to track frequency for each number
        mp = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        for num, count in mp.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res