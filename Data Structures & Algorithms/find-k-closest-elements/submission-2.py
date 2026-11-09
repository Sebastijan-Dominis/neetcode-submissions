class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        idx = None

        while l <= r:
            m = l + (r-l) // 2
            if arr[m] == x:
                idx = m
                break
            elif x > arr[m]:
                l = m + 1
                idx = l
            else:
                r = m - 1
                idx = l

        l, r = idx-1, idx
        res = []
        remaining = k

        while l >= 0 and r < len(arr) and remaining:
            if abs(arr[l] - x) < abs(arr[r] - x) or (abs(arr[l] - x) == abs(arr[r] - x) and arr[l] < arr[r]):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            remaining -= 1
        
        while remaining and l >= 0:
            res.append(arr[l])
            l -= 1
            remaining -= 1
        while remaining and r < len(arr):
            res.append(arr[r])
            r += 1
            remaining -= 1
        
        res.sort()
        return res