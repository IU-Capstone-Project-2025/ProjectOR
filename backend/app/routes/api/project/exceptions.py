class ProjectNotFoundError(Exception):
    def __init__(self, message="No project found."):
        self.message = message
        super().__init__(self.message)