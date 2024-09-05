class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        import numpy as np
        mat = np.zeros((m, n))
        answer = 0
        for x, y in indices:
            print(x, y)
            mat[:, y] += 1
            mat[x] += 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 == 1:
                    answer += 1


        return answer