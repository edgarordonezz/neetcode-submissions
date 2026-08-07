class TimeMap:

    def __init__(self):
        # map that can store multiple values for same key but with diff ts
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.mp[key])
        l = 0
        r = n - 1
        best = ""
        while l <= r:
            mid = l + (r - l) // 2 # get the middle
            ts, val = self.mp[key][mid]
            if ts > timestamp: # if ts is too large, we have to search left to find the smaller timestamp
                r = mid - 1
            else:
                best = val
                l = mid + 1
        return best