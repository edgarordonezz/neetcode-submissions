class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        // loop through strings
        for (String s : strs) {
            int[] count = new int[26];
            // loop through string chars
            for (char c : s.toCharArray()) {
                // count how many of each character
                count[c - 'a']++;
            }

            // converts integer array to key
            String key = Arrays.toString(count);

            // if this key isnt in the list, add it with a new list
            map.putIfAbsent(key, new ArrayList<>());
            // add curr string to the group for this key
            map.get(key).add(s);
        }

        // return all grouped anagrams
        return new ArrayList<>(map.values());

    }
}
