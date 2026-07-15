class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = [0] * (numCourses)
        def dfs(i):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False
            visited[i] = 1
            for u in graph[i]:
                if dfs(u) == False:
                    return False
            visited[i] = 2
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True