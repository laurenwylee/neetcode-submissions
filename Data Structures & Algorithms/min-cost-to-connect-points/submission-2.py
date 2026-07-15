class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        visited = set()
        minDist = [math.inf] * len(points)
        minDist[0] = 0

        # add len(points) nodes
        for _ in range(len(points)):
            cur = -1 # cur is the best unvisited node we've seen before

            # find the minimum distance
            for i in range(len(points)):
                if i in visited:
                    continue
                if cur == -1:
                    cur = i
                elif minDist[i] < minDist[cur]:
                    cur = i
            visited.add(cur)
            total += minDist[cur]

            # update the distances
            for nxt in range(len(points)):
                if nxt in visited:
                    continue
                pX = points[cur][0]
                pY = points[cur][1]
                nX = points[nxt][0]
                nY = points[nxt][1]
                dist = abs(pX-nX) + abs(pY - nY)
                minDist[nxt] = min(minDist[nxt], dist)
        return total
            
