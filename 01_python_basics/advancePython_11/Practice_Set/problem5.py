# My logic:
from json import dumps


def listComprehension(n, filePath):
    try:
        multiplicationList = [f"{n} X {i} = {n*i}" for i in range(1, 11)]
        tablecount = 0
        with open(f"{filePath}/tables.txt", "r") as f:
            content = f.read()

            if f"Table of {n} :" in content:
                return f"\nThe table of {n} already exists in the file!\n"

        with open(f"{filePath}/tables.txt", "a") as f:
            tablecount += 1
            f.write(f"(No: {tablecount}) Table of {n} : {dumps(multiplicationList, indent=2)}\n\n\n\n")

        return f"\n\nThe table of {n} is added successfully in the file\n\n {dumps(multiplicationList , indent=4)}"

    except Exception as e:
        return f"Error is coming: {e}"


n = int(input("Enter the number: "))
filePath = "advancePython_11/Practice_Set"
print(listComprehension(n, filePath))
# Harry bhai logic:

# n = 5

# tables = [n*i for i in range(1 , 11)]
# print(tables)