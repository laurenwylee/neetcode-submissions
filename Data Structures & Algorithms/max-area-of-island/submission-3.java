class Solution {
    public static int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int dfs(int[][] grid, int x, int y)
    {
        if(x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == 0)
        {
            return 0;
        }
        int sum = 1;
        grid[x][y] = 0;
        for(int i = 0; i < d.length; i++)
        {
            int dx = x + d[i][0];
            int dy = y + d[i][1];
            sum += dfs(grid, dx, dy);
        }
        return sum;
    }
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        for(int x = 0; x < grid.length; x++)
        {
            for(int y = 0; y < grid[0].length; y++)
            {
                if(grid[x][y] == 1)
                {
                    max = Math.max(max, dfs(grid, x, y));
                }
            }
        }
        return max;
    }
}
