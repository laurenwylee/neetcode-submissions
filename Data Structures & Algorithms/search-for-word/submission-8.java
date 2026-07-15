class Solution {
    int[][] d = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0,-1}};

    public boolean backtrack(int x, int y, int idx, String word, char[][] board)
    {
        if(idx == word.length() - 1)
        {
            return true;
        }
        for(int i = 0; i < d.length; i++)
        {
            int dx = x + d[i][0];
            int dy = y + d[i][1];
            if (dx < 0 || dx >= board.length || dy < 0 || dy >= board[0].length || board[dx][dy] != word.charAt(idx + 1))
            {
                continue;
            }
            char old = board[dx][dy];
            board[dx][dy] = '-';
            if(backtrack(dx, dy, idx + 1, word, board))
            {
                return true;
            }
            board[dx][dy] = old;
        }
        return false;

    }

    public boolean exist(char[][] board, String word) {
        for(int i = 0; i < board.length; i++)
        {
            for(int j = 0; j < board[0].length; j++)
            {
                if(board[i][j] == word.charAt(0))
                {
                    char old = board[i][j];
                    board[i][j] = '-';
                    if(backtrack(i, j, 0, word, board))
                    {
                        return true;
                    }
                    board[i][j] = old;
                }
            }
        }
        return false;

    }
}
