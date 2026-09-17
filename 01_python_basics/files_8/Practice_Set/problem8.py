


def copyThistxt(filePath , copyfilePath) :
    try:
        with open(filePath , "r") as f:
            content = f.read()
        with open(copyfilePath , "w") as f:
            result = f.write(content)
            if result :
                return "Copy of file created successfully"
            else :
                return "An error occur while making copying of the txt file"

    except FileNotFoundError as file:
        return f"Error coming and says {file}"

    except Exception as z :
        return f"Error saying {z}"


PathOfFile = "files_8/Practice_Set/this.txt"
CopyPathFile = "files_8/Practice_Set/this_copy.txt"

result = copyThistxt(PathOfFile , CopyPathFile)
print(result)