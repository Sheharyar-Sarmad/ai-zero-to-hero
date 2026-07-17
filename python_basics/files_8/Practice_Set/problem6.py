



def findPython(filePath, word):
    try:
        with open(filePath, "r") as f:
            content = f.read()

        if word.lower() in content.lower():
            return f"{word} found in {filePath}"
        else:
            return f"{word} not found in {filePath}"

    except FileNotFoundError:
        return f"The file {filePath} does not exist."

    except Exception as e:
        return f"An unexpected error occurred: {e}"


filePath = "files_8/Practice_Set/log.txt"
word = "Python"

result = findPython(filePath, word)
print(result)