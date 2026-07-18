class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Python automatically uses the first element for sorting
        intervals.sort()

        res = []

        # Stop the loop at pre-last interval to avoid additional if/else blocks
        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i+1][0]:
                # Non-overlapping -> just add it
                res.append(intervals[i])
            else:
                # Overlapping -> modify the upcoming interval in-place (if allowed)
                intervals[i+1] = [
                    min(intervals[i][0], intervals[i+1][0]),
                    max(intervals[i][1], intervals[i+1][1])
                ]
        
        # One remains to be added, since the loop doesn't catch it
        res.append(intervals[-1])
        return res