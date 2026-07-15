class Solution {
    public void dfs(int open, int close, List<String> result, StringBuilder str, int n)
    {
        if(open > n || close > n)
        {
            return;
        }
        if(open == close && open == n)
        {
            String joined = str.toString();
            result.add(joined);
            return;
        }
        if(open > close)
        {
            str.append(")");
            dfs(open, close+1, result, str, n);
            str.deleteCharAt(str.length() - 1);
        } 
        str.append("(");
        dfs(open+1, close, result, str, n);
        str.deleteCharAt(str.length() - 1);

    }
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        StringBuilder str = new StringBuilder();
        dfs(0, 0, result, str, n);
        return result;
    }
}
