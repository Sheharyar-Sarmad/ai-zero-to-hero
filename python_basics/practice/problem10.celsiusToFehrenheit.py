

def cToF(cNum) :
    try:
        if not(isinstance(cNum , int)) :
            return "Type error only integers are allowed!"
        else :
            return (cNum * 9/5) + 32
    except Exception as e:
        return f'Error is coming and saying this: {e}'
    
    
cNum = int(input("Enter your number: "));

print(cToF(cNum));
        