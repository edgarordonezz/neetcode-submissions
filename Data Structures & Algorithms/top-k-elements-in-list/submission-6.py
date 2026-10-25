class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mp = {}
        # count how many times it appears
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        freq = []
        for _ in range(len(nums) + 1):
            freq.append([])
        for num in mp:
            # freq[count] = nums that appear count times, e.g freq[3] = 3
            freq[mp[num]].append(num)
        # loop from the end to 0, each decrement by -1
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res