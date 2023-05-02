class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[2]))
        prefix = [0] * (trips[-1][2] + 1)
        
        for i in range(len(trips)):
            pass_, from_, to_ = trips[i]
            prefix[from_] += pass_
            prefix[to_] -= pass_
        prefix = list(accumulate(prefix))
        
        for i in range(len(prefix)):
            # prefix[i] += prefix[i-1]
            if prefix[i] > capacity:
                return False
        return True
        
        print(trips,prefix)
                   
    
    
'''
[[2,1,5],[3,3,7]]
​
1 2 3 4 5 6 7 8
2        -2
    3        -3
    
2 2 5 5 5 3 3 0
'''
