class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        # get number of rows
        m = len(matrix)
        # so then to get rows, we get the length of how many elements in each row 
        n = len(matrix[0])
        # low pointer
        low = 0
        # since indices are 0 based, we have to do -1
        high = (m * n) - 1
        while low <= high:
            # get the middle
            middle = low + (high - low) // 2 
            # convert flattened middle to row and column indices
            row = middle // n
            col = middle % n
            # if middle is the target, return true
            if matrix[row][col] == target:
                return True
            # if middle < target, that means that means that target is hiding in higher side
            # so we would increment our low
            elif matrix[row][col] < target: 
                low = middle + 1
            else:
                high = middle - 1
        return False