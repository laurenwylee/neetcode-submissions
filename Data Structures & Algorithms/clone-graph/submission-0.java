/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null)
        {
            return null;
        }
        HashMap<Integer, Node> graph = new HashMap<>();
        graph.put(node.val, new Node(node.val));
        Queue<Node[]> q = new ArrayDeque<>();
        q.add(new Node[]{node, graph.get(node.val)});
        while(!q.isEmpty())
        {
            Node[] curr = q.remove();
            List<Node> neigh = curr[0].neighbors;
            for(int i = 0; i < neigh.size(); i++)
            {
                if(!graph.containsKey(neigh.get(i).val))
                {
                    graph.put(neigh.get(i).val, new Node(neigh.get(i).val));
                    q.add(new Node[]{neigh.get(i), graph.get(neigh.get(i).val)});
                } 
                curr[1].neighbors.add(graph.get(neigh.get(i).val));
                
            }
        }
        return graph.get(node.val);
    }
}