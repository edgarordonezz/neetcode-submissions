import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency using a hashmap
        res = []
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        heap = []
        for num, freq in mp.items():
            heapq.heappush(heap, (freq, num))
            while len(heap) > k:
                heapq.heappop(heap)
        while heap:
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res