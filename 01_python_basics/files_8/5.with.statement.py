


def withStatment() :
    f = open("files_8/file.txt")
    print(f.read())
    f.close()
    
    # The same thing can be written using with statement and also more convinient and used in industry with real world projects:

    with open('files_8/file.txt') as f :
        print(f.read())

    # Now you dont have to explicitly close the file, like f.close()

withStatment()