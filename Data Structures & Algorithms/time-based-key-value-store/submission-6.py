class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            #do a binary search
            timestamps = self.store[key]
            l = 0
            r = len(timestamps) - 1

            while l <= r:
                mid = (l + r) // 2

                if timestamps[mid][0] > timestamp:
                    r = mid - 1
                elif timestamps[mid][0] < timestamp:
                    l = mid + 1
                else:
                    return timestamps[mid][1]
            if r >= 0:
                return timestamps[r][1]
            return ""
        else:
            return ""

