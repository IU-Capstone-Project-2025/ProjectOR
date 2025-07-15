class ApplicationNotFoundError(Exception):
    def __init__(self, message="No application found."):
        self.message = message
        super().__init__(self.message)
