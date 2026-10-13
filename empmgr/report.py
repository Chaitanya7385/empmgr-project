from collections import defaultdict

from .storage import load_employees


def department_summary():
    employees = load_employees()

    departments = defaultdict(list)

    for employee in employees:
        departments[employee["department"]].append(
            employee["salary"]
        )

    summary = {}

    for department, salaries in departments.items():
        summary[department] = {
            "headcount": len(salaries),
            "average_salary": sum(salaries) / len(salaries)
        }

    return summary