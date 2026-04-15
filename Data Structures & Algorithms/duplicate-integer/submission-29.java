class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable<Integer, Boolean> numbers = new Hashtable<>();
        for (int num : nums) {
            if (numbers.containsKey(num)) {
                return true;
            }
            numbers.put(num, true);
        }
        return false;
    }
}
