class APIError(Exception):
    """Describes an error triggered by a failing API call."""

    def __init__(self, message: str, code: int=500):
        """Creates a new APIError instance."""
        self.message = message
        self.code = code