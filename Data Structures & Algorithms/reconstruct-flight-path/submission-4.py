class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for a, b in tickets:
            edges[a].append(b)
        for x in edges:
            edges[x].sort()
            edges[x].reverse()
        path = []
        def dfs(node):
            while edges[node]:
                u = edges[node].pop()
                dfs(u)
            path.append(node)
        dfs("JFK")
        path.reverse()
        return path
            