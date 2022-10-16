class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals)
        result = []
        start , end = intervals[0][0],intervals[0][1]
        
        for i in intervals:
            if i[0] <= end:
                end = max(i[1],end)
            else:
                result.append([start, end])
                start,end = i[0], i[1]
        result.append([start,end])
        return result
