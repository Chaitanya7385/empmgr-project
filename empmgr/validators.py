# Input validation

import re


def parse_salary(text):
    try:
        salary = float(text)

        if salary < 0:
            return None

        return salary

    except ValueError:
        return None


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None