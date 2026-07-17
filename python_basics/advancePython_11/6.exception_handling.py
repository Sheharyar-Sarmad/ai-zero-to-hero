



def exception_handling() :
    try:      
        num = int(input("Hey, Enter number please!: "))

        print(f"\nIts a reversed table of {num}\n")

        for i in range(10 , 0 , -1) :
            print(f"{num} X {i} = {num * i}")
            with open(f"advancePython_11/tables/table_reverse_{num}.txt" , "w") as f:
                for i in range(10 , 0 , -1) :
                    line = f"{num} X {i} = {num * i}\n"
                    f.write(line)

        print(f"\nIts a simple table of the {num}\n")

        for i in range(1 , 11) :
            print(f"{num} X {i} = {num * i}")
            with open(f"advancePython_11/tables/table_simple_{num}.txt" , "w") as f:
                for i in range(1 , 11) :
                    line = f"{num} X {i} = {num * i}\n"
                    f.write(line)

    except ValueError:
        print("Please enter a valid integer")
       
    except Exception as e :
        print(f"\nAn error is coming and its saying this:\n{e}\n")

def aboutProgramm(name : str , dob : str , city : str , companyName : str):
    print(f'\nProgramm created by {name} ceo of {companyName} and born in {city} in {dob}\n')

exception_handling() 
aboutProgramm("Sheharyar" , "5/Aug/2010" , "Lahore" , "Webora Labs")