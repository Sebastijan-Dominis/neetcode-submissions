class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []

        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            else:
                intervals[i+1] = [
                    min(intervals[i][0], intervals[i+1][0]),
                    max(intervals[i][1], intervals[i+1][1])
                ]
        
        res.append(intervals[-1])
        return res