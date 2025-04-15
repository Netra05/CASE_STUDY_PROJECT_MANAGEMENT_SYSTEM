class EmployeeNotFoundException(Exception):
    def __init__(self, emp_id):
        super().__init__(f"Employee with ID {emp_id} not found in the system.")
