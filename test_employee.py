import pytest
from employee import employee_info

def test_employee_info():
    name = "Bob"
    emp_id = "E123"
    department = "IT"
    salary = 65000

    expected_output = (
        "Employee Name: Bob\n"
        "Employee ID: E123\n"
        "Department: IT\n"
        "Salary: 65000"
    )

    assert employee_info(name, emp_id, department, salary) == expected_output