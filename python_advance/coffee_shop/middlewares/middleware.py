
from database.security_config import SecurityConfig


class Middlewares:

    def __init__(self):
        pass

    @staticmethod
    def is_admin() -> bool:
        if not SecurityConfig.validate_session():
            print("\nYou must login as admin first!\n")
            return False

        return True