class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # n = len(mat)
        # answer = {}
        # for i in range(n):
        #     if (i, i) not in answer:
        #         answer[(i, i)] = mat[i][i]
        
        # a = 0
        # for k in range(n-1, -1, -1):
        #     if (a, k) not in answer:
        #         answer[(a, k)] = mat[a][k]
        #     a += 1
        # sumnum = sum(answer.values())
        # return sumnum

        n = len(mat)
        answer = []
        for i in range(len(mat)):
            answer.append(mat[i][i])
            if i != (n-1-i):
                answer.append(mat[i][n-1-i])
\
        return sum(answer)