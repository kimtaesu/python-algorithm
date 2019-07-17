from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            for j in range(int(n / 2)):
                row[j], row[~j] = row[~j], row[j]


a = Solution().rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], )
print(a)
