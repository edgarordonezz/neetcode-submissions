class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer>[] freq = new ArrayList[nums.length + 1];

        // Initialize freq array with nums.length + 1 empty lists
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        // Count the frequency of each number
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int number = entry.getKey(); // number
            int frequency = entry.getValue(); // count of number
            freq[frequency].add(number); // Access count and add number to it
        }

        int[] results = new int[k];
        int index = 0;
        // Store backwards since freq.length - 1 is the highest occuring number
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int num : freq[i]) {
                results[index++] = num;
                if (index == k) {
                    return results;
                }
            }
        }
        return results;
    }
}
