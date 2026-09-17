
# My logic
def PoemRead():
    with open("files_8/Practice_Set/poem.txt", "w") as f:
        poem_text = """
Twinkle, twinkle, little star,  
How I wonder what you are!  
Up above the world so high,  
Like a diamond in the sky.  
Twinkle, twinkle, little star.
"""
        f.write(poem_text)

    with open("files_8/Practice_Set/poem.txt", "r") as f:
        readResult = f.read()   

    word = ["Twinkle", "twinkle"]
    if word[0] in readResult or word[1] in readResult:
        print("\nTwinkle spotted")
    else:
        print("\nNo twinkle spotted")


PoemRead()

# Harry bhai logic
f = open("files_8/Practice_Set/poem.txt")
content = f.read()
if("twinkle" in content) :
    print("The word twinkle is present in the content")
else :
    print("The word twinkle is not present in the content")


# Ai logic:

def check_word(file_path, word):
    with open(file_path, "r") as f:
        content = f.read().lower()
    if word.lower() in content:
        print(f"{word} spotted!")
    else:
        print(f"{word} not found.")

check_word("files_8/Practice_Set/poem.txt", "twinkle")
check_word("files_8/Practice_Set/poem.txt", "star")