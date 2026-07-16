class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        water = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            leftMax = max(height[l], leftMax)
            rightMax = max(height[r], rightMax)
            
            if leftMax < rightMax:
                water += leftMax - height[l]
                l += 1
            else:
                water += rightMax - height[r]
                r -= 1
        
        return water