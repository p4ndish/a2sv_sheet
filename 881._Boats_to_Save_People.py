class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        s = set()
        c = Counter(people)
        N = len(people)
        l = 0
        r = N - 1
        while l <= r:
            f = people[l] + people[r]
            if f <= limit :
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                if people[l] > people[r]:
                    l += 1
                else:
                    r -= 1
                
        return res
            
