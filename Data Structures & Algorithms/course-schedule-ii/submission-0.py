class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for a, b in prerequisites:
            d[b].append(a)

        visited = [0] * numCourses
        cycle = False
        order = []
        def top_sort(nd):
            nonlocal cycle
            nonlocal order
            if visited[nd] == 1:
                cycle = True
                return
            if visited[nd] == 2:
                return

            visited[nd] = 1
            for n in d[nd]:
                top_sort(n)
            visited[nd] = 2
            order.append(nd)
        
        for course in range(numCourses):
            if visited[course] == 0:
                top_sort(course)
        
        if cycle:
            return []
        return order[::-1]