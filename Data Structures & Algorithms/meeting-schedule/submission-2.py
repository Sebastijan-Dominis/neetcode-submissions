"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Edge case - empty array
        if not intervals: return True

        # Sorting on intervals' start time - O(nlog(n)) time complexity
        intervals.sort(key = lambda i: i.start)

        # Still O(1) space complexity - just tracking the end of the previous interval
        prevEnd = intervals[0].end

        for i in intervals[1:]:
            # Current interval shouldn't start before previous has ended
            if i.start < prevEnd:
                return False
            # End of the current interval will be end of the previous one in the next iteration
            prevEnd = i.end
        
        # If the loop ended, there are no conflicts
        return True