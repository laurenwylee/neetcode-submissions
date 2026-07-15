class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def bfs(root):
            q = deque([root])
            visited.add(root)
            while q:
                nd = q.popleft()
                for u in graph[nd]:
                    if u not in visited:
                        q.append(u)
                        visited.add(u)
        
        num_components = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                num_components += 1
        return num_components
