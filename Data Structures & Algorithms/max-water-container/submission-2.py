class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        # width is (right - left) 
        # height = min(left, right)
        # total = width * height
        # keep updating max total while iterating through array
        max_total = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            total = width * height
            # if left side is greater than right side, decrease right
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

            max_total = max(max_total, total)
        return max_total