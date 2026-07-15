class Solution {
    public boolean dfs(int node, int parent, Set<Integer> visited, HashMap<Integer, ArrayList<Integer>> adj)
    {
        if(visited.contains(node))
        {
            return false;
        }
        visited.add(node);
        ArrayList<Integer> neighbors = adj.get(node);
        for(int i = 0; i < neighbors.size(); i++)
        {
            if(neighbors.get(i) == parent)
            {
                continue;
            }
            if(!dfs(neighbors.get(i), node, visited, adj))
            {
                return false;
            }
            
        }

        return true;

    }
    public boolean validTree(int n, int[][] edges) {
        int[] state = new int[n];
        Set<Integer> visit = new HashSet<>();
        HashMap<Integer, ArrayList<Integer>> adj = new HashMap<>();

        if(n-1 != edges.length)
        {
            return false;
        }

        for (int i = 0; i < n; i++) {
            adj.put(i, new ArrayList<>());
        }
        for(int i = 0; i < edges.length; i++)
        {
            adj.get(edges[i][0]).add(edges[i][1]);
            adj.get(edges[i][1]).add(edges[i][0]);
        }

        if(!dfs(0, -1, visit, adj)){return false;};
        return visit.size() == n;
    }
}
