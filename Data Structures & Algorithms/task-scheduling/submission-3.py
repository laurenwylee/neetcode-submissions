class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = defaultdict(int)
        for x in tasks:
            task_dict[x] += 1
        heap = []
        for x in task_dict:
            heapq.heappush(heap, -task_dict[x])
        queue = deque([])
        time = 1
        while queue or heap:
            if heap:
                c = heapq.heappop(heap)
                c += 1
                if c < 0:
                    queue.append((c, time + n))
            else:
                time = queue[0][1]
            if queue and queue[0][1] <= time:
                heapq.heappush(heap, queue.popleft()[0])
            time += 1
        return time - 1
            