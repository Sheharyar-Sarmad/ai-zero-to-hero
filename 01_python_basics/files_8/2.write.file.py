

st = 'Hey Harry you are amazing'

f = open("files_8/myfile.txt" , "w") # this w means i want to open this file in the write mode in which i can write data into and and it will store that data in that file as well.

writeFile = f.write(st)
if writeFile :
    print("Data transferred successfully") 
else :
    print("Data did'nt transferred")

f.close()
