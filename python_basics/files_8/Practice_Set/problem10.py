import time


def wipeOut(path1, path2):
    try:
        print("Wiping out the content of the file")
        time.sleep(2)

        with open(path1, "r") as file:
            result1 = file.read()

        with open(path2, "r") as file:
            result2 = file.read()

        if result1 != "" and result2 != "":
            with open(path1, "w") as file:
                pass
            with open(path2, "w") as file:
                pass
            return "Both file data wiped out successfully!"

        elif result1 != "" or result2 != "":
            with open(path1, "w") as file:
                pass
            with open(path2, "w") as file:
                pass
            return "One file has no content! \n but still the other file content wiped out successfully"
            
        else:
            return "There's no content in both files"

    except FileNotFoundError as fileEroor:
        return f"File not found and error is saying: {fileEroor}"

    except Exception as ex:
        return f"Error says this {ex}"


path_1 = "files_8/Practice_Set/this.txt"
path_2 = "files_8/Practice_Set/this_copy.txt"


result = wipeOut(path_1, path_2)
print(result)
