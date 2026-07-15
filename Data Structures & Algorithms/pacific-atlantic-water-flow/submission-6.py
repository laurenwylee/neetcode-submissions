class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacific = {}
        atlantic = {}
        def dfs(x, y, prev, isAtlantic):
            if x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0]):
                return
            if isAtlantic:
                if (x, y) in atlantic:
                    return
            else:
                if (x, y) in pacific:
                    return
            if heights[x][y] < prev:
                return
            if isAtlantic:
                atlantic[(x, y)] = 1
            else:
                pacific[(x, y)] = 1
            for dx, dy in d:
                dfs(x + dx, y + dy, heights[x][y], isAtlantic)
        for i in range(len(heights)):
            dfs(i, 0, -1, False)
        for i in range(1, len(heights[0])):
            dfs(0, i, -1, False)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, -1, True)
        for i in range(len(heights[0])):
            dfs(len(heights) - 1, i, -1, True)
        ret = []
        for x, y in pacific:
            if (x, y) in atlantic:
                ret.append([x, y])
        return ret
        