class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key):
            return ""
        
        l, r = 0, len(self.store[key]) - 1
        res = ""

        while l <= r:
            m = (l+r) // 2
            curr = self.store[key][m]

            if curr[1] < timestamp:
                res = curr[0]
                l = m + 1
            elif curr[1] > timestamp:
                r = m - 1
            else:
                return curr[0]
        
        return res