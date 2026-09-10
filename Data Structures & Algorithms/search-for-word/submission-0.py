class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # if word is present in grid, return true
        def backtrack(row, col, index, visited):
            if index == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
                
            if board[row][col] == word[index] and (row, col) not in visited:
                visited.add((row, col))
            # check up, left, right, bottom
                found = any([backtrack(row + 1, col, index + 1, visited),
                backtrack(row - 1, col, index + 1, visited),
                backtrack(row, col + 1, index + 1, visited),
                backtrack(row, col - 1, index + 1, visited)])
                visited.remove((row, col))
                return found
            else:
                return False
        for row in range(len(board)):
                for col in range(len(board[0])):
                    if backtrack(row, col, 0, set()):
                        return True
        return False