from dao.project_repo import ProjectRepositoryImpl
from entity.employee import Employee
from entity.project import Project
from entity.task import Task
from exception.employee_notfound import EmployeeNotFoundException
from exception.project_notfound import ProjectNotFoundException

def main():
    repo = ProjectRepositoryImpl()

    while True:
        print("\n--- Project Management System ---")
        print("1. Add Employee")
        print("2. Add Project")
        print("3. Add Task")
        print("4. Assign Project to Employee")
        print("5. Assign Task to Employee in a Project")
        print("6. Delete Employee")
        print("7. Delete Project")
        print("8. List Tasks for Employee in Project")
        print("9. View All Employees")
        print("10. View All Projects")
        print("11. View All Tasks")
        print("12. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                id = int(input("Enter Employee ID: "))
                name = input("Enter Name: ")
                designation = input("Enter Designation: ")
                gender = input("Enter Gender: ")
                salary = float(input("Enter Salary: "))
                project_id = int(input("Enter Project ID (or 0 if none): "))
                project_id = None if project_id == 0 else project_id

                emp = Employee(id, name, designation, gender, salary, project_id)
                if repo.create_employee(emp):
                    print("Employee added successfully.")
                else:
                    print("Failed to add employee.")

            elif choice == '2':
                id = int(input("Enter Project ID: "))
                name = input("Enter Project Name: ")
                desc = input("Enter Description: ")
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                status = input("Enter Status (started/dev/build/test/deployed): ")

                pj = Project(id, name, desc, start_date, status)
                if repo.create_project(pj):
                    print("Project added successfully.")
                else:
                    print("Failed to add project.")

            elif choice == '3':
                task_id = int(input("Enter Task ID: "))
                task_name = input("Enter Task Name: ")
                project_id = int(input("Enter Project ID: "))
                employee_id = int(input("Enter Employee ID (or 0 if not assigned): "))
                status = input("Enter Task Status (Assigned/Started/Completed): ")

                employee_id = None if employee_id == 0 else employee_id
                task = Task(task_id, task_name, project_id, employee_id, status)
                if repo.create_task(task):
                    print("Task created successfully.")
                else:
                    print("Failed to create task.")

            elif choice == '4':
                pid = int(input("Enter Project ID: "))
                eid = int(input("Enter Employee ID: "))
                if repo.assign_project_to_employee(pid, eid):
                    print("Project assigned to employee.")
                else:
                    print("Failed to assign project.")

            elif choice == '5':
                task_id = int(input("Enter Task ID: "))
                project_id = int(input("Enter Project ID: "))
                employee_id = int(input("Enter Employee ID: "))
                if repo.assign_task_to_employee_in_project(task_id, project_id, employee_id):
                    print("Task assigned to employee.")
                else:
                    print("Failed to assign task.")

            elif choice == '6':
                emp_id = int(input("Enter Employee ID to delete: "))
                if repo.delete_employee(emp_id):
                    print("Employee deleted.")
                else:
                    print("Employee deletion failed.")

            elif choice == '7':
                project_id = int(input("Enter Project ID to delete: "))
                if repo.delete_project(project_id):
                    print("Project deleted.")
                else:
                    print("Project deletion failed.")

            elif choice == '8':
                emp_id = int(input("Enter Employee ID: "))
                project_id = int(input("Enter Project ID: "))
                tasks = repo.get_all_tasks_for_employee_in_project(emp_id, project_id)
                if tasks:
                    print("\nTasks Assigned:")
                    for task in tasks:
                        print(f"Task ID: {task.get_task_id()}, Name: {task.get_task_name()}, Status: {task.get_status()}")
                else:
                    print("No tasks found or invalid IDs.")

            elif choice == '9':
                employees = repo.get_all_employees()
                if employees:
                    print("\n--- All Employees ---")
                    for emp in employees:
                        print(f"ID: {emp.get_id()}, Name: {emp.get_name()}, Designation: {emp.get_designation()}, Salary: {emp.get_salary()}, Project ID: {emp.get_project_id()}")
                else:
                    print("No employees found.")

            elif choice == '10':
                projects = repo.get_all_projects()
                if projects:
                    print("\n--- All Projects ---")
                    for p in projects:
                        print(f"ID: {p.get_id()}, Name: {p.get_name()}, Description: {p.get_description()}, Start Date: {p.get_start_date()}, Status: {p.get_status()}")
                else:
                    print("No projects found.")

            elif choice == '11':
                tasks = repo.get_all_tasks()
                if tasks:
                    print("\n--- All Tasks ---")
                    for t in tasks:
                        print(f"ID: {t.get_task_id()}, Name: {t.get_task_name()}, Project ID: {t.get_project_id()}, Employee ID: {t.get_employee_id()}, Status: {t.get_status()}")
                else:
                    print("No tasks found.")

            elif choice == '12':
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except EmployeeNotFoundException as e:
            print(f"Error: {e}")
        except ProjectNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()