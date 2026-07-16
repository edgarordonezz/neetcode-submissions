class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # if stack is empty or current height is greater than heigh in stack
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                # while stack is not empty and current height is less than height in stack
                while stack and heights[i] <= heights[stack[-1]]:
                    # get height from stack
                    height = heights[stack.pop()]
                    # if the stack is empty then widhth = current index
                    if not stack:
                        width = i
                    # else calculate width, -1 for inclusion only
                    else:
                        width = i - stack[-1] - 1
                    # get current area
                    area = width * height
                    # get max area
                    max_area = max(area, max_area)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            if not stack:
                width = len(heights)
            else:
                width = len(heights) - stack[-1] - 1
            # get current area
            area = width * height
            # get max area
            max_area = max(area, max_area)

        return max_area