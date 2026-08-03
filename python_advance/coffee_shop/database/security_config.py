import json
import os
from datetime import datetime, timedelta


class SecurityConfig:

    SESSION_FILE = "session.json"
    SESSION_DURATION = 7  # days

    @classmethod
    def create_session(cls, admin_id, name, email) -> bool:

        session_data = {
            "_id": admin_id,
            "name": name,
            "email": email,
            "created_at": datetime.now().isoformat(),
            "expires_at": (
                datetime.now() + timedelta(days=cls.SESSION_DURATION)
            ).isoformat()
        }

        with open(cls.SESSION_FILE, "w") as file:
            json.dump(session_data, file, indent=4)

        return True

    @classmethod
    def validate_session(cls) -> bool:

        # checking session file exists
        if not os.path.exists(cls.SESSION_FILE):
            return False

        try:
            with open(cls.SESSION_FILE, "r") as file:
                session = json.load(file)

            expiry_time = datetime.fromisoformat(
                session["expires_at"]
            )

            # session expired
            if datetime.now() > expiry_time:

                cls.destroy_session()

                return False

            return True

        except Exception:

            return False

    @classmethod
    def get_session(cls):

        if not cls.validate_session():
            return None
        
        with open(cls.SESSION_FILE, "r") as file:
            return json.load(file)

    @classmethod
    def destroy_session(cls) -> bool:

        if os.path.exists(cls.SESSION_FILE):
            os.remove(cls.SESSION_FILE)

        return True