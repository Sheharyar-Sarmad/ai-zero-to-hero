import time as waqtDiQadarKarKaka

class Programmer:
    company = 'Microsoft 🏢'

    def __init__(self, name, salary, role, pinCode):
        self.name = name
        self.salary = salary
        self.role = role
        self.pinCode = pinCode
        
        print("\n🔄 Creating Programmer Profile...")
        waqtDiQadarKarKaka.sleep(2)
        print("✅ Profile Created Successfully!\n")

    def Showdata(self):
        print("══════════════════════════════")
        print("👨‍💻 PROGRAMMER DETAILS")
        print("══════════════════════════════")
        print(f"🏢 Company   : {self.company}")
        print(f"🧑 Name       : {self.name} 🥳")
        print(f"💼 Role       : {self.role} 🚀")
        print(f"💰 Salary     : ₹{self.salary:,} 💵")
        print(f"📍 Pin Code   : {self.pinCode} 📮")
        print("══════════════════════════════\n")


name = input("🧑 Enter your name: ")
salary = int(input("💰 Enter your salary: "))
role = input("💼 Enter your role: ")
pinCode = input("📍 Enter your pin code: ")

ProgrammerInfo = Programmer(name, salary, role, pinCode)
ProgrammerInfo.Showdata()