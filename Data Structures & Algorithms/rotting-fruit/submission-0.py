class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        num_fresh = 0
        q = deque([])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append([x,y])
                if grid[x][y] == 1:
                    num_fresh += 1
        count = 0
        while q and num_fresh > 0:
            count += 1
            for i in range(len(q)):
                currx, curry = q.popleft()
                for x, y in d:
                    if currx + x >= 0 and currx + x < len(grid) and curry + y >= 0 and curry + y < len(grid[0]) and grid[currx+x][curry+y] == 1:
                        grid[currx+x][curry+y] = 2
                        num_fresh -= 1
                        q.append([x + currx, y + curry])
                if num_fresh <= 0:
                    break
        if num_fresh <= 0:
            return count
        return -1
