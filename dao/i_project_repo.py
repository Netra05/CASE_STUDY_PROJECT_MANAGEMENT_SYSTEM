from abc import ABC, abstractmethod
from entity.employee import Employee
from entity.project import Project
from entity.task import Task

class IProjectRepository(ABC):

    @abstractmethod
    def create_employee(self, emp: Employee):
        pass

    @abstractmethod
    def create_project(self, pj: Project):
        pass

    @abstractmethod
    def create_task(self, task: Task):
        pass

    @abstractmethod
    def assign_project_to_employee(self, project_id: int, employee_id: int):
        pass

    @abstractmethod
    def assign_task_to_employee_in_project(self, task_id: int, project_id: int, employee_id: int):
        pass

    @abstractmethod
    def delete_employee(self, emp_id: int):
        pass

    @abstractmethod
    def delete_project(self, project_id: int):
        pass

    @abstractmethod
    def get_all_tasks_for_employee_in_project(self, emp_id: int, project_id: int):
        pass

    @abstractmethod
    def get_all_employees(self) -> list:
        pass

    @abstractmethod
    def get_all_projects(self) -> list:
        pass

    @abstractmethod
    def get_all_tasks(self) -> list:
        pass
