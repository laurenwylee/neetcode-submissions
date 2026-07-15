class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d.keys():
            self.d[key].append([timestamp, value])
        else:
            self.d[key] = [[timestamp, value]]

    # [1,3,4]
    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            # binary search
            values = self.d[key]
            l = 0
            r = len(values) - 1
            while l <= r:
                p = (l + r) // 2
                if values[p][0] == timestamp:
                    return values[p][1]
                else:
                    # [1,2,4]
                    # [1,3,4]
                    if values[p][0] < timestamp:
                        print("Test")
                        print(timestamp)
                        l = p + 1
                        if l < len(values) and values[l][0] > timestamp:
                            return values[l-1][1]
                        elif l >= len(values):
                            return values[l-1][1]
                    else:
                        r = p - 1
                        if r > 1 and values[r][0] < timestamp:
                            return values[r][1]
                        if r == 1:
                            return values[r][1]
            return ""
        else:
            return ""