a = "kaise ho"

for letter,index in enumerate(a):
    if letter == " ":
        break
    print(f"loop breaked {index}")