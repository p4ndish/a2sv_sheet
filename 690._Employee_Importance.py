"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
​
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        print(employees[0].id)
        
        
        adj = defaultdict(list)
        for employee in employees:
            adj[employee.id].append(employee.importance)
            adj[employee.id].append(employee.subordinates)
            
        # print(adj)
            
        visited = set()
        self.res = 0 
        def dfs(eId, visited):
            # if 
            visited.add(eId)
            sums = 0 
            # print(sums)
            self.res += adj[eId][0]
            for employe in adj[eId][1]:
                if employe not in visited:
                    dfs(employe, visited)
            
        
        dfs(id, visited)
        return self.res
        
'''
1 : [5, [2,3]]
2 : [3, []]
3 : [3, []]
'''
