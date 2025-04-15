from dao.i_project_repo import IProjectRepository
from util.db_conn_util import DBConnUtil
from entity.employee import Employee
from entity.project import Project
from entity.task import Task
from exception.employee_notfound import EmployeeNotFoundException
from exception.project_notfound import ProjectNotFoundException

class ProjectRepositoryImpl(IProjectRepository):

    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def create_employee(self, emp: Employee) -> bool:
        try:
            if emp.get_project_id():
                check_proj_query = "SELECT * FROM Project WHERE Id = ?"
                self.cursor.execute(check_proj_query, (emp.get_project_id(),))
                if not self.cursor.fetchone():
                    raise ProjectNotFoundException(emp.get_project_id())

            check_employee_query = "SELECT * FROM Employee WHERE id = ?"
            self.cursor.execute(check_employee_query, (emp.get_id(),))
            if self.cursor.fetchone():
                raise Exception(f"Employee with ID {emp.get_id()} already exists.")

            query = "INSERT INTO Employee(id, name, Designation, Gender, Salary, Project_id) VALUES (?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, (
                emp.get_id(), emp.get_name(), emp.get_designation(), emp.get_gender(), emp.get_salary(),
                emp.get_project_id()))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error creating employee:", e)
            return False

    def create_project(self, pj: Project) -> bool:
        query = "INSERT INTO Project(Id, ProjectName, Description, Start_date, Status) VALUES (?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(query, (
                pj.get_id(),
                pj.get_name(),
                pj.get_description(),
                pj.get_start_date(),
                pj.get_status()
            ))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error creating project:", e)
            return False

    def create_task(self, task: Task) -> bool:
        query = "INSERT INTO Task(task_id, task_name, project_id, employee_id, Status) VALUES (?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(query, (
                task.get_task_id(), task.get_task_name(), task.get_project_id(),
                task.get_employee_id(), task.get_status()))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error creating task:", e)
            return False

    def assign_project_to_employee(self, project_id: int, employee_id: int) -> bool:
        try:
            check_query = "SELECT * FROM Employee WHERE id = ?"
            self.cursor.execute(check_query, (employee_id,))
            if not self.cursor.fetchone():
                raise EmployeeNotFoundException(employee_id)

            check_proj = "SELECT * FROM Project WHERE Id = ?"
            self.cursor.execute(check_proj, (project_id,))
            if not self.cursor.fetchone():
                raise ProjectNotFoundException(project_id)

            query = "UPDATE Employee SET Project_id = ? WHERE id = ?"
            self.cursor.execute(query, (project_id, employee_id))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error assigning project:", e)
            return False

    def assign_task_to_employee_in_project(self, task_id: int, project_id: int, employee_id: int) -> bool:
        try:
            query = "UPDATE Task SET project_id = ?, employee_id = ? WHERE task_id = ?"
            self.cursor.execute(query, (project_id, employee_id, task_id))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error assigning task:", e)
            return False

    def delete_employee(self, emp_id: int) -> bool:
        try:
            self.cursor.execute("SELECT * FROM Employee WHERE id = ?", (emp_id,))
            if not self.cursor.fetchone():
                raise EmployeeNotFoundException(emp_id)

            query = "DELETE FROM Employee WHERE id = ?"
            self.cursor.execute(query, (emp_id,))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error deleting employee:", e)
            return False

    def delete_project(self, project_id: int) -> bool:
        try:
            self.cursor.execute("SELECT * FROM Project WHERE Id = ?", (project_id,))
            if not self.cursor.fetchone():
                raise ProjectNotFoundException(project_id)

            query = "DELETE FROM Project WHERE Id = ?"
            self.cursor.execute(query, (project_id,))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error deleting project:", e)
            return False

    def get_all_tasks_for_employee_in_project(self, emp_id: int, project_id: int) -> list:
        query = "SELECT * FROM Task WHERE employee_id = ? AND project_id = ?"
        self.cursor.execute(query, (emp_id, project_id))
        rows = self.cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(Task(task_id=row.task_id, task_name=row.task_name, project_id=row.project_id, employee_id=row.employee_id, status=row.Status))
        return tasks

    def get_all_employees(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM Employee")
            rows = self.cursor.fetchall()
            employees = []
            for row in rows:
                emp = Employee(row.id, row.name, row.Designation, row.Gender, row.Salary, row.Project_id)
                employees.append(emp)
            return employees
        except Exception as e:
            print("Error fetching employees:", e)
            return []

    def get_all_projects(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM Project")
            rows = self.cursor.fetchall()
            projects = []
            for row in rows:
                project = Project(row.Id, row.ProjectName, row.Description, row.Start_date, row.Status)
                projects.append(project)
            return projects
        except Exception as e:
            print("Error fetching projects:", e)
            return []

    def get_all_tasks(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM Task")
            rows = self.cursor.fetchall()
            tasks = []
            for row in rows:
                task = Task(row.task_id, row.task_name, row.project_id, row.employee_id, row.Status)
                tasks.append(task)
            return tasks
        except Exception as e:
            print("Error fetching tasks:", e)
            return []
