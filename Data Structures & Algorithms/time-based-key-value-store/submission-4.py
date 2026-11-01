class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key):
            return ""

        res = ""
        values = self.store[key]

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            curr = values[m]
            curr_value, curr_timestamp = curr[0], curr[1]

            if curr_timestamp < timestamp:
                res = curr_value
                l = m + 1
            elif curr_timestamp > timestamp:
                r = m - 1
            else:
                return curr_value
        
        return res