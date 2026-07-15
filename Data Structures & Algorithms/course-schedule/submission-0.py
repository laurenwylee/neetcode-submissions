class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for a, b in prerequisites:
            d[b].append(a)

        visited = [0] * numCourses
        cycle = False
        def top_sort(nd):
            nonlocal cycle
            if visited[nd] == 1:
                cycle = True
                return
            if visited[nd] == 2:
                return

            visited[nd] = 1
            for n in d[nd]:
                top_sort(n)
            visited[nd] = 2
        
        for course in range(numCourses):
            if visited[course] == 0:
                top_sort(course)
        
        return not cycle