class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        start, end = intervals[0]
        res = [intervals[0]]
        for st, en in intervals[1:]:
            if st <= end:
                #error so make the end to "en"
                end = max(en, end)
                res[-1][1] = end
            else:
                res.append([st,en])
                start = st
                end = en
        print(res)
        return res
