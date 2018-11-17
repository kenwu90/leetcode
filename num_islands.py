class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        y_len = len(grid)
        x_len = len(grid[0])

        check = [[False for j in range(x_len)] for i in range(y_len)]
        cnt = 0

        def dfs(i, j):
            if i < 0 or i >= y_len or j < 0 or j>= x_len or check[i][j]:
                return
            else:
                check[i][j] = True
                if grid[i][j] == '1':
                    dfs(i+1, j)
                    dfs(i-1, j)
                    dfs(i, j+1)
                    dfs(i, j-1)
                return

        for i in range(y_len):
            for j in range(x_len):

                if check[i][j]:
                    continue

                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

                check[i][j] = True

        return cnt


if __name__ == '__main__':
    s = Solution()
    s.numIslands([['1', '0'], ['1', '0']])