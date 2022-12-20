class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary, maxSalary = min(salary), max(salary)
        n = len(salary) - 2
        
        return (sum(salary) - minSalary - maxSalary) / n