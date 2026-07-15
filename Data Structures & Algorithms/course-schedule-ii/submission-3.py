class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = [0] * (numCourses)
        def dfs(i, output):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False
            visited[i] = 1
            for u in graph[i]:
                if dfs(u, output) == False:
                    return False
            visited[i] = 2
            output.append(i)
            return True
        output = []
        for i in range(numCourses):
            if dfs(i, output) == False:
                return []
        return output