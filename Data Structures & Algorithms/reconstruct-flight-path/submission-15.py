class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for a, b in tickets:
            edges[a].append(b)
        for x in edges:
            edges[x].sort()
            edges[x].reverse()
        path = []
        def dfs(src):
            while edges[src]:
                u = edges[src].pop()
                dfs(u)
            path.append(src)
        dfs("JFK")
        path.reverse()
        return path
        # def dfs(src):
        #     # print(path)
        #     if len(path) == len(tickets) + 1:
        #         return True
        #     temp = edges[src].copy()
        #     for i, dest in enumerate(temp):
        #         edges[src].pop(i)
        #         path.append(dest)
        #         if dfs(dest) == True:
        #             return True
        #         path.pop()
        #         edges[src].insert(i, dest)
        #     return False
        # dfs("JFK")
        # return path
