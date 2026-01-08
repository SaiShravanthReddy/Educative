# 2373. Largest Local Values in a Matrix
# 40 mins to read, solve and debug

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Traverse row, i -1, i, i +1,
        # Traverse column j - 1, j, j+1
        # Limit i and j can go from 1 to len(row) - 2

        ans = []

        row_index = 1

        while row_index <= len(grid[0]) - 2:
            # print("row_index", row_index)
            row = []
            column_index = 1

            while column_index <= len(grid[0]) - 2:
                # print("column_index", column_index)

                temp_row_index = row_index - 1
                row_max = 0

                while temp_row_index <= row_index + 1:
                    # print(
                    #     "row_max",
                    #     row_max,
                    #     "grid",
                    #     grid[temp_row_index][column_index - 1 : column_index + 2],
                    # )
                    row_max = max(
                        row_max,
                        max(grid[temp_row_index][column_index - 1 : column_index + 2]),
                    )

                    temp_row_index += 1

                row.append(row_max)
                column_index += 1

            ans.append(row)
            row_index += 1

        return ans

# Best space
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        res[i][j] = max(res[i][j], grid[r][c])

        return res

# Best time, but dont use 
import numpy as np

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        a = np.asarray(grid)
        r = np.maximum.reduce([a[:, 0:-2], a[:, 1:-1], a[:, 2:]])
        c = np.maximum.reduce([r[0:-2, :], r[1:-1, :], r[2:, :]])

        return c.tolist()