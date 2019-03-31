"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        def cmp_fn(x, y):
            if x.start != y.start:
                return cmp(x.start, y.start)
            return cmp(x.end, y.end)

        def merge_interval(a, b):
            if a.end >= b.start:
                return Interval(a.start, max(a.end, b.end))
            return None
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(cmp = cmp_fn)
        idx = 0
        current_interval = intervals[0]
        for i in range(1, n):
            res = merge_interval(current_interval, intervals[i])
            if res is not None:
                current_interval = res
            else:
                intervals[idx] = current_interval
                idx += 1
                current_interval = intervals[i]
        intervals[idx] = current_interval
        return intervals[:idx + 1]
