class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if they overlap, get earliest time and latest end time and merge them
        intervals.sort() # sort first
        res = [intervals[0]]
        # res = [[1,3]]
        # 3 <= 5
        # res = [[1, 5]], updated end = res[1] 
        # start from 1 to end since we'll be comparing with previous intervals
        for start, end in intervals[1:]:
            old_start, old_end = res[-1]
            if start <= old_end:
                # 1 <= 3, yes -> so update res to res = [[1, max(3, 5)]]
                res[-1][1] = max(end, old_end)
            else:
                res.append([start, end])
        return res
                