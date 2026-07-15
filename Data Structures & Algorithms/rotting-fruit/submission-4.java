class Solution {

    public int orangesRotting(int[][] grid) {
        int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Queue<int[]> q = new ArrayDeque<>();
        int freshCount = 0;
        for(int i = 0; i < grid.length; i++)
        {
            for(int j = 0; j < grid[0].length; j++)
            {
                if(grid[i][j] == 2)
                {
                    q.add(new int[]{i, j});
                }
                if(grid[i][j] == 1)
                {
                    freshCount++;
                }
            }
        }

        if (freshCount == 0) return 0;

        int layer = 0;
        while(!q.isEmpty())
        {
            // System.out.println("in here");
            int sz = q.size();
            boolean rottedThisRound = false;
            for(int i = 0; i < sz; i++)
            {
                int[] coord = q.remove();
                int x = coord[0];
                int y = coord[1];
                for(int j = 0; j < d.length; j++)
                {
                    int dx = x + d[j][0];
                    int dy = y + d[j][1];
                    if(dx < 0 || dx >= grid.length || dy < 0 || dy >= grid[0].length || grid[dx][dy] != 1)
                    {
                        continue;
                    }
                    grid[dx][dy] = 2;
                    q.add(new int[]{dx, dy});
                    rottedThisRound = true;
                    freshCount--;
                }
                
            }
            if (rottedThisRound) layer++;
        }
        if(freshCount != 0)
        {
            return -1;
        }
        return layer;
    }
}
