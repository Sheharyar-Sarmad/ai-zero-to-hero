letter = """
Dear <|Name|>,
you are selected!
<|Date|>...
"""

name = input("Enter your name: ")
date = input("Enter date: ")

# This approach is chaining in .replace function and this is super helpfull:
print(letter.replace("<|Name|>", name).replace("<|Date|", date))
