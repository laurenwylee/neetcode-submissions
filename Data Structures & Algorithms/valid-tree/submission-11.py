class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [-1] * n
        stack = []
        stack.append((0 , - 1))
        while stack:
            nd, parent = stack.pop()
            visited[nd] = 1
            for u in graph[nd]:
                if u == parent:
                    continue 
                if visited[u] != -1:
                    return False
                stack.append((u, nd))
        for i in range(n):
            if visited[i] != 1:
                return False
        return True