import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dont need sqrt
        # first lets get the distance between points and pair them with their points
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist, (x, y)))
        res = []
            

        
        for _ in range(k):
           x, y = heapq.heappop(heap)
           res.append(y)
        return res
