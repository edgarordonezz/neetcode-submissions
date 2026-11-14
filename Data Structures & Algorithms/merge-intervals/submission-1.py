class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last = res[-1] # get the last interval
            last_end = last[1] # get the end time of the last interval added to res
            if start <= last_end:
                last[1] = max(end, last_end)
            else:
                res.append([start, end])
        return res