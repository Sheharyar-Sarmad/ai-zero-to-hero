def findingLineOfString(filePath, word):
    try:
        with open(filePath, "r") as f:
            line_numbers = []  # list to store line numbers
            for i, line in enumerate(f, start=1):  # loop line by line
                if word.lower() in line.lower():
                    line_numbers.append(i)
        
        if line_numbers:
            return f"{word} found on line(s): {line_numbers}"
        else:
            return f"{word} not found in any line"

    except Exception as e:
        return f"Error: {e}"


File = "files_8/Practice_Set/line.txt"
word = 'PYTHON'

result = findingLineOfString(File, word)
print(result)