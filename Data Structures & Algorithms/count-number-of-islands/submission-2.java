class Solution {
    public void dfs(char[][] grid, int x, int y)
    {
        int[][] d = { {1, 0}, {-1, 0}, {0, 1}, {0,-1}};
        for(int i = 0; i < d.length; i++)
        {
            int dx = x + d[i][0];
            int dy = y + d[i][1];
            if(dx >= 0 && dx < grid.length && dy >= 0 && dy < grid[0].length && grid[dx][dy] == '1')
            {
                grid[dx][dy] = '0';
                dfs(grid, dx, dy);
            }
        }

    }
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int x = 0; x < grid.length; x++)
        {
            for(int y = 0; y < grid[0].length; y++)
            {
                if(grid[x][y] == '1')
                {
                    count++;
                    grid[x][y] = '0';
                    dfs(grid, x, y);
                }
            }
        }
        return count;
    }
}
