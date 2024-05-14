class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxGold = 0
        
        def dfsBacktrack(i, j, currentGold):
            nonlocal maxGold
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            goldInCurrentCell = grid[i][j]
            currentGold += goldInCurrentCell
            maxGold = max(maxGold, currentGold)
            temp = grid[i][j]
            grid[i][j] = 0
            dfsBacktrack(i + 1, j, currentGold)
            dfsBacktrack(i - 1, j, currentGold)
            dfsBacktrack(i, j + 1, currentGold)
            dfsBacktrack(i, j - 1, currentGold)
            grid[i][j] = temp
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfsBacktrack(i, j, 0)
        
        return maxGold