class Solution {
    private boolean dfs(ArrayList<Integer> order, int node, List<List<Integer>> graph, int[] state) {
        if (state[node] == 1) return false;    // cycle found
        if (state[node] == 2) return true;     // already finished

        state[node] = 1; // mark visiting

        for (int neigh : graph.get(node)) {
            if (!dfs(order, neigh, graph, state))
            {
                return false;
            }
        }

        state[node] = 2; // mark done
        order.add(node);
        return true;
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        ArrayList<Integer> order = new ArrayList<>();
        // build adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            graph.get(pre[0]).add(pre[1]);
        }

        int[] state = new int[numCourses]; // 0 = unvisited, 1 = visiting, 2 = visited

        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0) {
                if (!dfs(order, i, graph, state))
                {
                    return new int[0];
                }
            }
        }
        int[] res = new int[numCourses];
        for(int i = 0; i < order.size(); i++)
        {
            res[i] = order.get(i);
        }
        return res;
    }
}

