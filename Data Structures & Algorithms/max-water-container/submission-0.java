class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int res = 0;

        while (left < right) {
            // calculate the area by finding the minimum and multiplying by
            // distance between right and left
            // l = 1, h = 6 equals 1 * 6 - 1 = 5
            int area = Math.min(heights[left], heights[right]) * (right - left);
            // compare res and current area
            res = Math.max(res, area);
            // if left pointer is less than right pointer increment left
            if (heights[left] < heights[right]) {
                left++;
            // if left pointer is greater than right pointer decrement right
            } else {
                right--;
            }
        }
        // return result
        return res;
    }
}
