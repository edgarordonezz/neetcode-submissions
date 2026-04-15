class Solution {
    public boolean isValidSudoku(char[][] board) {
        /* 
        Valid if each row and column
        contains 1-9 no duplicates
        each 3 x 3 contains 1-9 no duplicates
        */
        Set<Character>[] row = new HashSet[9];
        Set<Character>[] col = new HashSet[9];
        Set<Character>[] square = new HashSet[9];
        for (int i = 0; i < 9; i++) {
            row[i] = new HashSet<>();
            col[i] = new HashSet<>();
            square[i] = new HashSet<>();
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                // c stores 0,0
                char val = board[i][j];
                // Skip periods
                if (val == '.') continue;

                // if row already contains value return false
                // else add it to set
                if (row[i].contains(val)) return false;
                row[i].add(val);

                // if col already contains value return false
                // else add it to set
                if (col[j].contains(val)) return false;
                col[j].add(val);

                // find box index by dividing by 
                int boxIndex = (i / 3) * 3 + (j / 3);
                if (square[boxIndex].contains(val)) return false;
                square[boxIndex].add(val);
            }
        }
        return true;
    }
}
