# def starter():
#     print("\nPrint 1 for addition")
#     print("Print 2 for substraction")
#     print("Print 3 for multiplication")
#     print("Print 4 for division")
#     print("Print exit for division\n")  # Fixed typo: should be "Print 'exit' to quit"

# def calculator(choice, num1: float, num2: float):
#     try:
#         # KEY FIX 1: Convert string choice to int if it's a number
#         if choice.isdigit():
#             choice = int(choice)
#         else:
#             print("\nInvalid choice!\nChoice must be only 1,2,3,4 or 'exit'!\n")
#             return None
            
#         if choice not in [1, 2, 3, 4]:
#             print("\nInvalid choice!\nChoice must be only 1,2,3,4!\n")
#             return None
        
#         if choice == 1:
#             return num1 + num2
#         elif choice == 2:
#             return num1 - num2
#         elif choice == 3:
#             return num1 * num2
#         elif choice == 4:
#             if num2 == 0:
#                 print("\nCannot divide by zero!\n")
#                 return None
#             return num1 / num2
            
#     except Exception as e:
#         print(f"An error occurred due to {e}")
#         return None

# def ender():
#     print("\nThanks for using our calculator!")
#     print("Developed by Sheharyar Sarmad By Love\n")

# while True:
#     starter()
#     choice = input("\nProvide your choice (1, 2, 3, 4, or 'exit'): ")
    
#     # KEY FIX 2: Check for exit BEFORE asking for numbers
#     if choice.lower() == "exit":
#         ender()
#         break
    
#     # KEY FIX 3: Use float instead of int for division
#     try:
#         num1 = float(input("\nProvide your first number: "))
#         num2 = float(input("Provide your second number: "))
#     except ValueError:
#         print("\nInvalid number input! Please enter valid numbers.\n")
#         continue
    
#     result = calculator(choice, num1, num2)
#     if result is not None:
#         print(f"\nResult: {result}\n")
        

print(eval(input("Enter calculation: ")) if input("Enter calculation: ") else "Invalid")