class Solution {
    public void dfs(int node, int[] visited, HashMap<Integer, ArrayList<Integer>> graph)
    {
        // if(visited[node] != 0)
        // {
        //     return false;
        // }
        visited[node] = 1;
        ArrayList<Integer> neighbors = graph.get(node);
        for(int i = 0; i < neighbors.size(); i++)
        {
            if(visited[neighbors.get(i)] == 0)
            {
                dfs(neighbors.get(i), visited, graph);
            }
        }
        // return true;
    }
    public int countComponents(int n, int[][] edges) {
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        for(int i = 0; i < n; i++)
        {
            graph.put(i, new ArrayList<Integer>());
        }
        for(int i = 0; i < edges.length; i++)
        {
            graph.get(edges[i][0]).add(edges[i][1]);
            graph.get(edges[i][1]).add(edges[i][0]);
        }

        int count = 0;
        int[] visited = new int[n];
        for(int i = 0; i < n; i++)
        {
            if(visited[i] == 0)
            {
                dfs(i, visited, graph);
                count++;
            }
            // if(dfs(i, visited, graph))
            // {
            //     count++;
            // }
        }

        return count;
    }
}
