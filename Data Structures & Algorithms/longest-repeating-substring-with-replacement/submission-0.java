class Solution {
    public int characterReplacement(String s, int k) {
        // AABABBA k = 1
        // replace one A in the middle with B and form AABBBBA
        // substring BBBB has the longest repeating letters which is 4
        HashMap<Character, Integer> count = new HashMap<>();
        int max = 0;
        int left = 0;
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // count occurence of key
            count.put(c, count.getOrDefault(c, 0) + 1);
            // Determine if max or count c is higher
            max = Math.max(max, count.get(c));

            // while window size - max char occurrence is greater than k
            while ((i - left + 1) - max > k) {
            // store start of window
                char leftChar = s.charAt(left);
            // shrink the substring by removing the left pointer
                count.put(leftChar, count.get(leftChar) - 1);
                left++;
            }
            // determine between the max and window 
            maxLen = Math.max(maxLen, i - left + 1);
        }
        return maxLen;
    }
}
