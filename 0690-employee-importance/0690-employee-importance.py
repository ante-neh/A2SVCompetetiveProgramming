"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importanceVal = {}
        visited = set()
        totalImportance = 0
        
        for employee in employees:
            importanceVal[employee.id] = employee.importance
            for e in employee.subordinates:
                graph[employee.id].append(e)
            
        def dfs(node):
            nonlocal totalImportance
            visited.add(node)
            totalImportance += importanceVal[node]
            
            for sub in graph[node]:
                if not sub in visited:
                    dfs(sub)
                    
        dfs(id)
        
        return totalImportance
            
        