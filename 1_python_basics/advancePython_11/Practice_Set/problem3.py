# My logic:

from json import dumps


def listComprehension(n) :
   try:
        multiplicationList = [f"{n} X {i} = {n*i}" for i in range(1, 11)]
        return  dumps( multiplicationList , indent=2 ) 
        
   except Exception as e :
       return f"Error is coming: {e}"
       

n = int(input("Enter the number: "))
listComprehension(n)
# Harry bhai logic:

n = 5

tables = [n*i for i in range(1 , 11)]
print(tables)