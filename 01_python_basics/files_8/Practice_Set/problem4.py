# # My logic:

# import time

# def replaceWord(filePath, word, updatedWord):
#     print("Replacing the word...")
#     time.sleep(1.5)

#     # Step 1: Read file content
#     with open(filePath, "r") as f:
#         content = f.read()

#     # Step 2: Check if the word exists
#     if word in content:
#         # Step 3: Replace the word
#         content = content.replace(word, updatedWord)
#         # Step 4: Write updated content back
#         with open(filePath, "w") as f:
#             f.write(content)
#         return f"Program worked fine: word replaced, {word} replaced by {updatedWord}"
#     else:
#         return "Word not found in the file"

# # Example usage
# print(replaceWord("files_8/Practice_Set/donkey.txt", "donkey", "######"))

# # Harry bhai logic:

# word = "donkey"

# with open("files_8/Practice_Set/donkey.txt" , "r") as f :
#     content = f.read()

# contentNew.replace(word , "donkey")

# with open("files_8/Practice_Set/donkey.txt" , "w") as f :
#     f.write(contentNew)