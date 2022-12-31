class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        
        salary.sort()
        a = sum(salary[1:n-1])
        return (a /(n-2) )
