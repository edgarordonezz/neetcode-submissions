class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Use HashMap to get count of them using map functions
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) { // if set contains num already
                return true; // return true
            }
            seen.add(num); // add num to set
        }
        return false; // return false if num is not in set indicating there is no dupes
    }
} // O(n) worst case we traverse the whole array 