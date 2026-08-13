

def generateTables(n) :
    table = ""
    for i in range(1 , 11) :
        table += f"{n} X {i} = {n * i}\n"
    with open(f"files_8/Practice_Set/tables/table_{n}.txt" , "w") as f :
        result = f.write(table)
    if(result) :
        print("Tables are created successfully")
    else: 
        print("Error occur while creating these tables")

for i in range(2 , 21) :
    generateTables(i) 
