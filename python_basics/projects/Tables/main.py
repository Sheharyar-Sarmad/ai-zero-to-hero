import os

n = int(input("Enter your number: "))

# create folder if not exists
os.makedirs("Tables", exist_ok=True)

file_name = f"Tables/table_{n}.txt"

# write table into file
with open(file_name, "w") as f:
    for i in range(1, 11):
        f.write(f"{n} X {i} = {n * i}\n")

# read and display file content
with open(file_name, "r") as f:
    print(f.read())