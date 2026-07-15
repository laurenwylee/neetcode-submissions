class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        visited = [0] * n
        has_cycle = False

        def dfs(i, parent):
            nonlocal has_cycle
            if visited[i] == 1:
                has_cycle = True
                return
            if visited[i] == 2:
                return

            visited[i] = 1
            for u in d[i]:
                if u != parent:
                    dfs(u, i)
            visited[i] = 2
        
        dfs(0, -1)
        return not has_cycle and len(edges) == n - 1