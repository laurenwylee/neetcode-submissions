class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> q = new ArrayDeque<>();
        int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for(int x = 0; x < grid.length; x++)
        {
            for(int y = 0; y < grid[0].length; y++)
            {
                if(grid[x][y] == 0)
                {
                    q.add(new int[]{x, y});
                }
            }
        }

        int layer = 0;
        while(!q.isEmpty())
        {
            int sz = q.size();
            for(int i = 0; i < sz; i++)
            {
                int[] curr = q.remove();
                int x = curr[0];
                int y = curr[1];

            
                if(grid[x][y] == Integer.MAX_VALUE){grid[x][y] = layer;}

                for(int j = 0; j < d.length; j++)
                {
                    int dx = x + d[j][0];
                    int dy = y + d[j][1];
                    if(dx < 0 || dx >= grid.length || dy < 0 || dy >= grid[0].length || grid[dx][dy] != Integer.MAX_VALUE )
                    {
                        continue;
                    }
                    q.add(new int[]{dx, dy});
                }
            }
            layer++;
        }
    }
}
