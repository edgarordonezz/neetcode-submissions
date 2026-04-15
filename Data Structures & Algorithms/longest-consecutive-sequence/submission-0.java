class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int longest = 0;

        // add all numbers to the set
        for (int num : nums) {
            seen.add(num);
        }

        for (int num : nums) {
            // only start when you see the smallest number
            if (!seen.contains(num - 1)) {
                // set curr to number
                int curr = num;
                // if only one number then sequence = 1
                int streak = 1;

                // while set contains the next occuring number
                while (seen.contains(curr + 1)) {
                    // check next number
                    curr++;
                    // increase streak
                    streak++;
                }
                // track longest streak
                longest = Math.max(longest, streak);
            }
        }
        return longest;
    }
}
