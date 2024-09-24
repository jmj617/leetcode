class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        
        for j in range(len(grid[0])):
            max_len = 0
            for i in range(len(grid)):
                leni = len(str(grid[i][j]))
                max_len = max(max_len, leni)
            answer.append(max_len)

        return answer