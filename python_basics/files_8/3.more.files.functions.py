 
import json 
f = open("files_8/file.txt")

# Reading multiple lines:
# lines = f.readlines()

# if lines :
#     print(json.dumps(lines , indent=2))
#     print("")
#     print(type(lines).__name__)
#     print("Lines read successfully")
#     f.close()
# else :
#     print("Lines did'nt read, there was an error while reading the file data")
#     f.close()

# Reading line:

# line1 = f.readline()
# print(json.dumps(line1 , indent=2) , type(line1))

# line2 = f.readline()
# print(json.dumps(line2 , indent=2) , type(line2))

# line3 = f.readline()
# print(json.dumps(line3 , indent=2) , type(line3))

# line4 = f.readline()
# print(json.dumps(line4 , indent=2) , type(line4))

# line5 = f.readline()
# print(json.dumps(line5 == "", indent=2) , type(line5))

line = f.readline()

while line != "" :
    print(line)
    line = f.readline()