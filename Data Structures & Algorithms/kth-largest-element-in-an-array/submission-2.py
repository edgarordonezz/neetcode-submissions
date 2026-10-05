import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # negate nums in place for less space
        for i in range(len(nums)):
            nums[i] = nums[i]

        # heapify: O(logn)
        heapq.heapify(nums)

        # heap = [-5 at the top, -4 next]

        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]