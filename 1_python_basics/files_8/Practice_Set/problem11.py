import os
import time

def renameFile(nameBefore, nameAfter):
    try:
        # Get the current file name automatically
        exactFileNameBeforeRenaming = os.path.basename(nameBefore)
        print(f"Renaming file: {exactFileNameBeforeRenaming}")
        time.sleep(2)

        os.rename(nameBefore, nameAfter)

        return f"{nameBefore} is updated into {nameAfter}"

    except FileNotFoundError as fileError:
        return f"File not found and error is saying: {fileError}"

    except Exception as e:
        return f"Error is saying: {e}"


# User input
nameOfFileInput = input("Enter new file name (without extension): ")

nameBefore = "files_8/Practice_Set/kiase ho.txt"
nameAfter = f"files_8/Practice_Set/{nameOfFileInput}.txt"

# Rename the file
result = renameFile(nameBefore, nameAfter)
print(result)