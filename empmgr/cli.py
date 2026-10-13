# Menu and user interaction
# The . means we are importing from the same package

from rich.console import Console
from rich.table import Table


from .storage import load_employees, save_employees
from .validators import parse_salary


def add_employee(employees, name, email, department, salary):
    next_id = max(
        (employee["id"] for employee in employees),
        default=0
    ) + 1

    employees.append({
        "id": next_id,
        "name": name,
        "email": email,
        "department": department,
        "salary": salary
    })


def main():
    employees = load_employees()

    while True:
        print("\n=== Employee Manager ===")
        print("1. List employees")
        print("2. Add employee")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            table = Table(title="Employees")

            table.add_column("ID")
            table.add_column("Name")
            table.add_column("Department")
            table.add_column("Salary")

            for employee in employees:
                table.add_row(
                    str(employee["id"]),
                    employee["name"],
                    employee["department"],
                    f"{employee['salary']:,.2f}"
                )
            Console().print(table)

        elif choice == "2":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            department = input("Department: ").strip()
            salary = parse_salary(input("Salary: "))

            if not name or salary is None:
                print("Invalid input - employee not added.")
                continue

            add_employee(
                employees,
                name,
                email,
                department,
                salary
            )

            save_employees(employees)

        elif choice == "3":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()