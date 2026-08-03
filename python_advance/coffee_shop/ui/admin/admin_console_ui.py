



from middlewares.middleware import Middlewares


class ConsoleUIAdmin:
    def __init__(self, admin_name: str = None):
        self.admin_name = admin_name

    def starter(self):
        print("=" * 60)
        print("🔐 THE COZY CUP SHOP - ADMIN PANEL 🔐".center(60))
        print("=" * 60)

        if Middlewares.is_admin():
            print("✅ Administrator Login Successful\n")
            print(f"👤 Admin : {self.admin_name}")
            print("🟢 Session Status : Active")
        else:
            print("❌ Administrator Not Logged In")
            print("🔒 Please login to continue.")

        print("=" * 60)

    def ender(self):
        print("\n" + "=" * 60)
        print("🔐 EXITING ADMIN PANEL 🔐".center(60))
        print("=" * 60)

        if Middlewares.is_admin():
            print("✅ Admin session closed successfully.\n")
            print(f"👤 Admin : {self.admin_name}")
        else:
            print("⚠ No administrator was logged in.")

        print("=" * 60)