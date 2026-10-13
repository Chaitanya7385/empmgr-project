# Employee data structure
# Defines what an Employee looks like.

from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    email: str
    department: str
    salary: float

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "salary": self.salary
        }