class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force solution
        # for every index I will find the maximum value in the window
        res = []
        # need to figure out when it'll stop though
        # so if len(nums) = 7
        # last window has to contain 5,6,7 without going out of bounds
        # so we need to iterate all the way up to 5
        # let len(nums) = m 
        # so the general case will be range = m - k + 1 
        # that will give us 7 - 3 + 1 = 5
        for i in range(0, len(nums) - k + 1):
            # window start is at i and end is at k
            window = nums[i: i+k]
            # get the max element of the window
            max_element = max(window)
            # insert max element into array
            res.append(max_element)

        return res