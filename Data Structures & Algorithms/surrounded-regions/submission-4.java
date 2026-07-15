class Solution {
    int[][] d = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void dfs(char[][] board, int x, int y)
    {
        for(int i = 0; i < d.length; i++)
        {
            int dx = d[i][0] + x;
            int dy = d[i][1] + y;
            if(dx < 0 || dx >= board.length || dy < 0 || dy >= board[0].length)
            {
                continue;
            }
            if(board[dx][dy] == 'O')
            {
                board[dx][dy] = '#';
                dfs(board, dx, dy);
            }
        }
    }

    public void solve(char[][] board) {
        for(int i = 0; i < board[0].length; i++)
        {
            if(board[0][i] == 'O')
            {
                board[0][i] = '#';
                dfs(board, 0, i);
            }
            if(board[board.length - 1][i] == 'O')
            {
                board[board.length-1][i] = '#';
                dfs(board, board.length-1, i);
            }
        }
        for(int i = 1; i < board.length-1; i++)
        {
            if(board[i][0] == 'O')
            {
                board[i][0] = '#';
                dfs(board, i, 0);
            }
            if(board[i][board[0].length - 1] == 'O')
            {
                board[i][board[0].length - 1] = '#';
                dfs(board, i, board[0].length-1);
            }
        }

        for(int x = 0; x < board.length; x++)
        {
            for(int y = 0; y < board[0].length; y++)
            {
                if(board[x][y] == '#')
                {
                    board[x][y] = 'O';
                }else if (board[x][y] == 'O')
                {
                    board[x][y] = 'X';
                }
            }
        }
        
    }
}
