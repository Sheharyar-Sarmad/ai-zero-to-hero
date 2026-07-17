
def main( ):
    try :
        a = int(input('Enter your number: '))
        print(a)
        return

    except Exception as e :
        print(f"Error says: {e}")
    # The else block will run when the try code runs successfully or else if it goes in except block then it will not go in the else block.

    # Conslucion: We run the else block to check wheter our try block code runs successfully or not
    else :
        print("I am inside else")
        return 
    # Always use finally in functions and infact, its right usecase always come inside a function
    # The finally blocks code always runs no matter what , if the try runs or not if the except runs or not if the else runs or not , it breaks all the rules and run on its own without any hesitation.
    finally :
        print("Hey i am inside of finally")
        return 



main()