class Solution {

    public String encode(List<String> strs) {
        if (strs.isEmpty()) return "";
        // get size of string
        StringBuilder sb = new StringBuilder();
        // for each string append length n followed by
        // # so its like 3#hey
        for (String str : strs) {
            sb.append(str.length()).append('#').append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            // j goes up until it finds the delimeter
            while (str.charAt(j) != '#') {
                j++;
            }
            // finds the length by basically doing str.subtring(0, 1)
            // str.substring == 4
            int length = Integer.parseInt(str.substring(i, j));
            // i now equals 1 + 1 so it starts at the beginning of the string
            i = j + 1;
            // j is now at the end of string 
            j = i + length;
            // add from 2 to 6 to build the string
            res.add(str.substring(i, j));
            // start over if theres multiple delimeters
            i = j;
        }
        return res;
    }
}
