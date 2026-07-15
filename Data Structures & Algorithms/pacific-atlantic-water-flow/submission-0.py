class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        qp = deque([])
        qa = deque([])
        pacific = defaultdict(int)
        atlantic = defaultdict(int)

        for x in range(len(heights)):
            pacific[(x, 0)] += 1
            atlantic[(x, len(heights[0]) - 1)] += 1
            qp.append([x, 0])
            qa.append([x, len(heights[0]) - 1])
        for y in range(len(heights[0])):
            pacific[(0, y)] += 1
            atlantic[(len(heights) - 1, y)] += 1
            qp.append([0, y])
            qa.append([len(heights) - 1, y])
        
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while qp:
            currx, curry = qp.popleft()
            for x, y in d:
                if currx + x >= 0 and currx + x < len(heights) and curry + y >= 0 and curry + y < len(heights[0]) and heights[currx + x][curry+y] >= heights[currx][curry] and (currx + x, curry + y) not in pacific:
                    pacific[(currx + x, curry + y)] += 1
                    qp.append([currx + x, curry + y])
        while qa:
            currx, curry = qa.popleft()
            for x, y in d:
                if currx + x >= 0 and currx + x < len(heights) and curry + y >= 0 and curry + y < len(heights[0]) and heights[currx + x][curry+y] >= heights[currx][curry] and (currx + x, curry + y) not in atlantic:
                    atlantic[(currx + x, curry + y)] += 1
                    qa.append([currx + x, curry + y])
        result = []
        for x, y in pacific:
            if (x, y) in atlantic:
                result.append([x, y])
        return result
