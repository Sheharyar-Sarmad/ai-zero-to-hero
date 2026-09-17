

import time

def identicalFiles(path1 , path2) :
    try:
        print("Proccessing that the files are identicals or not: ")
        time.sleep(2)

        with open(path1 , "r") as f :
            result1 = f.read()
        with open(path2 , "r") as f :
            result2 = f.read()
        if result1 == result2 :
            return f"Yes the content in the files are same"
        else: 
            return "No content in the files are not same"

    except FileNotFoundError as file :
        return f"Error says {file}"
    
    except Exception as uu :
        return f"Error coming and its saying {uu}"

path_1 = "files_8/Practice_Set/this.txt"
path_2 = "files_8/Practice_Set/this_copy.txt"

print(identicalFiles(path_1 , path_2))