class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        num = float("inf")
        
        for i,(x1,y1) in enumerate(points):
            dx = x - x1
            dy = y - y1
            
            if dx * dy == 0 and abs(dx + dy) < num:
                res = i
                num = abs(dx + dy)
        return res
