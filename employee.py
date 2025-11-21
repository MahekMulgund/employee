# employee.py
def employee_info(name, emp_id, department, salary):
    """
    Returns a formatted string containing employee details.
    """
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
if __name__ == "__main__":
    name = "Bob"
    emp_id = "E123"
    department = "IT"
    salary = 65000

    print(employee_info(name, emp_id, department, salary))



