class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        options = self.map[key]
        l = 0
        r = len(options) - 1
        closest = None
        while l <= r:
            mid = l + (r-l) // 2
            if options[mid][0] == timestamp:
                return options[mid][1]
            elif options[mid][0] > timestamp:
                r = mid - 1
            else:
                if not closest or closest[0] < options[mid][0]:
                    closest = options[mid]
                l = mid + 1
        if not closest:
            return ""
        return closest[1]