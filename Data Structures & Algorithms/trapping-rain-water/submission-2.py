class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # min(height) * min(width) = amount
        # total = total + amount
        l = 0
        r = len(height) - 1
        leftMax = 0
        rightMax = 0
        total = 0
        while l < r:
            # get max of left and right
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
        
            if leftMax < rightMax:
                total += leftMax - height[l]
                l += 1
            else:
                total += rightMax - height[r]
                r -= 1
        return total