class TimeMap:

    def __init__(self):
        # create a defaultdict(list) since we're grouping together (key, value, time)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.store:
            entries = self.store[key]
            l = 0
            r = len(entries) - 1
            while l <= r:
                mid = (l + r) // 2
                v, t = entries[mid]
                if t <= timestamp:
                    l = mid + 1
                    res = v
                else:
                    r = mid - 1
        return res