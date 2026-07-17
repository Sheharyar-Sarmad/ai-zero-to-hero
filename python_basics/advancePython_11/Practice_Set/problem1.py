def rightFile(path1 , path2 , path3 , content1 , content2 , content3) :
   try:
    with (
        open(path1 , "w") as f1 ,
        open(path2 , "w") as f2  ,
        open(path3 , "w") as f3 
    ) :
        content1 = content1 
        content2 = content2
        content3 = content3

        f1.write(content1)
        f2.write(content2)
        f3.write(content3)
    
   except FileNotFoundError as notFound :
        print(f"Error says file not found and {notFound}")

   except Exception as e :
        print(f'Error coming and its saying {e}')

   else :
        print(f"\nThe program is created by Sheharyar Sarmad\nThe CEO of Webora Labs and he borns in Lahore in 5/Aug/2010\n")

   finally :
        print("\nThanks for your using our program\n")

path1 = "advancePython_11/Practice_Set/file1.txt"
path2 = "advancePython_11/Practice_Set/file2.txt"
path3 = "advancePython_11/Practice_Set/file3.txt"

content1 = input("Enter first(1st) file content: ")
content2 = input("Enter second(2nd) file content: ")
content3 = input("Enter third(3rd) file content: ")

rightFile(path1 , path2 , path3 , content1 , content2 , content3)