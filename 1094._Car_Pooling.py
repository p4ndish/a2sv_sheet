class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        0 1 2 3 4 5 6 7  = 5
          2 0 0 0-2
              3 0 0 0-3
          2 2 5 5 3 3 0
        '''
        
        prefix = [0]*1001
        for trip in trips:
            passangers, begin, end = trip
            prefix[begin] += passangers
            prefix[end] -= passangers
            
        # sums = prefix[0]
        if prefix[0] > capacity:
            return False
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1] 
            if prefix[i] > capacity:
                return False
        return True
​
