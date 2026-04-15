class Solution {
    public int[] productExceptSelf(int[] nums) {
        // create postfix
        int postfix = 1;
        int[] res = new int[nums.length];
        res[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            // res[0] = 1
            // res[1] = (res[0]=1) * (nums[0]=1) = 1
            // res [2] = (res[1]=1) * (nums[1]=2) = 2
            // res [3] = (res[2]=2) * (nums[2]=4) = 8
            res[i] = res[i - 1] * nums[i - 1];
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            // res[3] = 8 * 1
            // postfix = 6
            res[i] = res[i] * postfix;
            postfix = postfix * nums[i];
        }
        return res;
    }
}  
