class ProjectNotFoundException(Exception):
    def __init__(self, project_id):
        super().__init__(f"Project with ID {project_id} not found in the system.")
