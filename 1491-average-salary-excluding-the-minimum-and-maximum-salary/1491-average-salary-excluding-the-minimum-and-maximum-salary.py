class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = max(salary)
        min_salary = min(salary)
        n = 0
        total = 0
        for i in salary :
            if i != max_salary and i != min_salary :
                total += i 
                n += 1
        return total / n
                
        