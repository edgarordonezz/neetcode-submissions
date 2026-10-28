class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_amount = min(height[l], heigt[r]) * (r - l)
        # total to be greatest means greatest height and biggest width
        l = 0
        r = len(heights) - 1
        max_amount = 0
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            total = height * width
            max_amount = max(max_amount, total)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_amount
