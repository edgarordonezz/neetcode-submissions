class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # here we will make the heap after we figure out distances
        # so first we will iterate through array and get each euclidean distance
        distances = []
        closest = []
        for x,y in points:
            dist = x * x + y * y
            # prioritize the euclidean distance, so it goes first
            key = (dist, (x, y))
            distances.append(key)
        heapq.heapify(distances)

        for _ in range(k):
            # unpack tuples, a =dist, b = points, we need points here
            a, b = heapq.heappop(distances)
            closest.append(b)
        return closest