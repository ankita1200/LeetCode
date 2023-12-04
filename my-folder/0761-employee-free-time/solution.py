"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints=[]
        for i in schedule:
            for x in i:
                ints.append(x)
        ints.sort(key=lambda x: x.start)
        merged = []
        for sch in ints:
            if merged and merged[-1].end>=sch.start:
                merged[-1].end=max(sch.end,merged[-1].end)
            else:
                merged.append(sch)
        free = []
        for i in range(1,len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
        return free

