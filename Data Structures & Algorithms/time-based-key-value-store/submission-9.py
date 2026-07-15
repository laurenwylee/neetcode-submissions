class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        results = self.d[key]
        if results == []:
            return ""
        l = 0
        r = len(results) - 1
        greatest = -1
        idx = -1
        while l <= r:
            m = (l + r) // 2
            if results[m][1] == timestamp:
                return results[m][0]
            elif results[m][1] < timestamp:
                greatest = max(results[m][1], greatest)
                idx = m
                l = m + 1
            else:
                r = m -1
        if greatest != -1:
            return results[idx][0]
        return ""
