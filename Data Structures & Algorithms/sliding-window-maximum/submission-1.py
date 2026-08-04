import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Optimal Solution
        res = []
        heap = [] # declare heap
        for i in range(len(nums)): # insert values into heap(negate them since python's heap is a min heap)
            heapq.heappush(heap, (-nums[i], i)) # insert negative value and index into heap
            if i >= k - 1: # once the window is complete, check for staleness and append if in window
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap) 
                res.append(-heap[0][0]) # append the max to res
        return res
            