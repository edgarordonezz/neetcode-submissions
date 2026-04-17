class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for row in range(9)] # 9 rows
        cols = [set() for col in range(9)] # 9 cols
        boxes = [set() for box in range(9)] # 9 individual boxes
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        return True