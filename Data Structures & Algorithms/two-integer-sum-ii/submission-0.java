class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            // keep track of sum
            int sum = numbers[left] + numbers[right];
            if (sum == target){
                // 1-indexed means starting from 1 not 0
                return new int[]{left + 1, right + 1};
                // if sum is too small means that left is too small
            } else if (sum < target ) {
                left++;
            } else {
                right--;
            }
        }
        return new int[0];
    }
}
