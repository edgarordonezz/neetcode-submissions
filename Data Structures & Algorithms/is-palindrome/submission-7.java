class Solution {
    public boolean isPalindrome(String s) {
        int first = 0;
        int last = s.length() - 1;
        
        while (first < last) {
            // while char at first is not a letter or digit increment
            while (first < last && !Character.isLetterOrDigit(s.charAt(first))) {
                first++;
            }
            // while char at last is not a letter or digit increment
            while (first < last && !Character.isLetterOrDigit(s.charAt(last))) {
                last--;
            }
            // if char at first does not equal char at last return false
            if (Character.toLowerCase(s.charAt(first)) != Character.toLowerCase(s.charAt(last))) {
                return false;
            }
            // increment and decrement to meet in the middle if palindrome
            first++;
            last--;

        }
        return true;
    }
}
