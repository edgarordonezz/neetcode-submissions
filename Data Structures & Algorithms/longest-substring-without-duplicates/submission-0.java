class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> seen = new HashSet<>();
        int left = 0;
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            // while present char does not equal next char
            // add char to sequence
            char curr = s.charAt(i);
            // if current char is already in the window, move left until its gone
            while (seen.contains(curr)) {
            // if char already exists, remove so we can test a new sequence
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(curr);
            // i - left + 1 because say 4 = i and 2 = left
            // length should be (4-2) = 2 + 1 since 2,3,4 should be included
            max = Math.max(max, i - left + 1);
        }
        return max;
    }
}
