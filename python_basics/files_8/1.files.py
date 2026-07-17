
'''
Difference between RAM and Files: 

The random access memory (RAM) is volatile , and its memory and data losts once the programm terminates. In order to persist the data forever, we use files

A file is data stored in storage device. A python programm can talk to the file by reading its content and by adding content into it.

RAM == volatile
HDD == non-volatile

 When you run the programm in the RAM , its not persist and go away the programm terminates. In simple, RAM is a temporary memory.

When you store your data in files using python programm , the data saved in it was a permanent data and it didnt go away when you terminates the programm.
'''

'''
a = "a is a very long string used for extracting the email of the users"

emails = [...]

just imagine it took 3 seconds to run the programm and then the you print the emails but when you will terminates the programm , the data of the emails will go forever because RAM is volatile
'''

'''
There are two types of files:

text files(.txt , .c  etc...)
binary files(.jpeg , .data etc...)
'''

f = open("files_8/file.txt", "r")
data = f.read()
print(data)
f.close()