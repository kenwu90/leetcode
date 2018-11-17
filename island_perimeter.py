class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        result = 0
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return result
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt = 0
                if grid[i][j] == 0:
                    continue
                    
        return result

s = Solution()

island_list = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(s.islandPerimeter(island_list))

