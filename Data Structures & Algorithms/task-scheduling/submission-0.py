class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurence = defaultdict(int)
        for task in tasks:
            occurence[task] += 1
        h = []
        for task in occurence:
            heapq.heappush(h, (-occurence[task]))
        q = deque([])
        time = 0
        while h or q:
            time += 1
            if h:
                cnt = 1 + heapq.heappop(h)
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        return time