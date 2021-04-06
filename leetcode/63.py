class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # reuse obstacleGird as the dp array, reduce the space complexity
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                while j < n:
                    obstacleGrid[0][j] = 0
                    j += 1
                break
            else:
                obstacleGrid[0][j] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                while i < m:
                    obstacleGrid[i][0] = 0
                    i += 1
                break
            else:
                obstacleGrid[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]
