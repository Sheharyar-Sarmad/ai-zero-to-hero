import time
import json
import re

def replaceWordsWithMask(filePath, words):
    print("Reading the file...")
    time.sleep(1)  # just for effect

    # Step 1: Read the file content
    with open(filePath, "r") as f:
        content = f.read()
    
    print("\n--- Original Content ---")
    print(content)

    # Step 2: Replace each word with '#' of the same length (case-insensitive)
      word in words:
        updatedWord = "#" * len(word)
        # Use re.sub with flags=re.IGNORECASE for case-insensitive replacement
        content = re.sub(re.escape(word), updatedWord, content, flags=re.IGNORECASE)

    # Step 3: Write the updated content back to the file
    with open(filePath, "w") as f:
        f.write(content)

    print("\n--- Updated Content ---")
    print(content)

    return f"\nProgram worked fine: {len(words)} words replaced.\nWords replaced:\n{json.dumps(words, indent=2)}"


# List of words to replace
words = ["donkey", "bad", "ganda", "bagairat"]

# Path to your file
file_path = "files_8/Practice_Set/donkey2.txt"

# Run the function
print(replaceWordsWithMask(file_path, words))