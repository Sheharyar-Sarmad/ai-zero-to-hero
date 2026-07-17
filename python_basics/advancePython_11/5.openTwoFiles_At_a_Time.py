



def openTwoFiles(filePath1 , filePath2) :
    with(
        open(filePath1 , "w") as f1 ,
        open(filePath2 , "w") as f2
    ) :
        f1.write("Hello File 1\n")
        f2.write("Hello File 2\n")


openTwoFiles("advancePython_11/file1.txt" , "advancePython_11/file2.txt")