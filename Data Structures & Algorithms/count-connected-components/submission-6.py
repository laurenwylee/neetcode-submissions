class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(i):
            stack = []
            stack.append(i)
            visited[i] = 1
            while stack:
                nd = stack.pop()
                for u in graph[nd]:
                    if visited[u] == 0:
                        visited[u] = 1
                        stack.append(u)

        count = 0
        visited = [0] * (n)
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1
        return count