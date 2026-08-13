



names = ["Ali", "Ahmed", "Sara"]
marks = [85, 90, 78]

NameDict = {}

for name,mark in zip(names , marks) :
    NameDict[name] = mark
    
print(NameDict);