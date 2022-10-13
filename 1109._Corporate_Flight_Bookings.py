class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        s = [0]*(n+2)
        
        for (start, end, seat) in bookings:
            s[start] += seat
            s[end + 1] += -seat
        
        res = [0]
        # print(s)
        for i in range(1, len(s)):
            res.append(res[-1]+s[i])
        # print(res)
        # print(list(accumulate(s)))
        # for i in range()
        return list(accumulate(s))[1:-1]
