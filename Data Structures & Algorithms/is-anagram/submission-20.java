class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            int count = countS.getOrDefault(s.charAt(i), 0) + 1;

            char charT = t.charAt(i);
            int count2 = countT.getOrDefault(t.charAt(i), 0) + 1;

            countS.put(charS, count);
            countT.put(charT, count2);
        }

        return countS.equals(countT);
    }
}
