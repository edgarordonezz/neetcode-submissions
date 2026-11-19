class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1: 0, 0 -> 0, 0
        # 2: 0, 1 -> 1, 0
        # 3: 1, 0 -> 0, 1
        # 4: 1, 1 -> 1, 1
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()