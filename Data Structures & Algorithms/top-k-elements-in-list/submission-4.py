class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        # count how many times it appears
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        freq = []
        # freq store the number, and how many times it occurs
        for num in mp:
            freq.append((mp[num], num))
        freq.sort(reverse=True)
        res = []
        for count, num in freq[:k]:
            res.append(num)
        return res