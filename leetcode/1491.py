class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)

        total_sal = sum(salary) - min_sal - max_sal
        num_salaries = len(salary) - 2

        return total_sal / num_salaries
