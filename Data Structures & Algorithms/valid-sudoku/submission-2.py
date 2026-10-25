class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # condition 1: 1-9 no duplicates (rows)
        # condition 2: 1-9 no duplicates (columns)
        # condition 3: each block no duplicates
        # valid if all these pass
        set_r = [set() for _ in range(9)]
        set_c = [set() for _ in range(9)]
        set_block = [set() for _ in range(9)]

        for r in range(len(board)): # rows
            for c in range(len(board[0])): # columns
                # once at a cell, box is (r // 3, c // 3)
                if board[r][c] == ".":
                    continue
                br = r // 3
                bc = c // 3
                box = br * 3 + bc
                val = board[r][c]
                if val in (set_r[r]) or val in (set_c[c]) or val in (set_block[box]):
                    return False
                else:
                    set_r[r].add(val)
                    set_c[c].add(val)
                    set_block[box].add(val)
        return True