studentDic = {}

# ➕ Add Student
def addStudent():
    name = input("Enter student name: ")

    if name == "":
        print("Please enter name")
        return

    if name in studentDic:
        print("Student already exists")
        return

    student_class = int(input("Enter student class: "))
    studentDic[name] = student_class

    print("Student added successfully!")
    print("Current Dictionary:", studentDic)


# ✏️ Update Student (Rename + Change Class)
def updateStudent():
    old_name = input("Enter existing student name: ")

    if old_name not in studentDic:
        print("Student not found")
        return

    new_name = input("Enter new name: ")
    new_class = int(input("Enter new class: "))

    # Rename logic
    studentDic.pop(old_name)
    studentDic[new_name] = new_class

    print("Student updated successfully!")
    print("Current Dictionary:", studentDic)


# ❌ Delete Student
def deleteStudent():
    name = input("Enter student name to delete: ")

    if name in studentDic:
        studentDic.pop(name)
        print("Student deleted successfully!")
        print("Current Dictionary:", studentDic)
    else:
        print("Student not found")


# 📄 View All Students
def viewStudents():
    if len(studentDic) == 0:
        print("No students available")
    else:
        print("\n===== STUDENT LIST =====")
        for name, class_num in studentDic.items():
            print(f"Name: {name} | Class: {class_num}")


# 🔥 MAIN MENU LOOP
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        addStudent()

    elif choice == "2":
        updateStudent()

    elif choice == "3":
        deleteStudent()

    elif choice == "4":
        viewStudents()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.")