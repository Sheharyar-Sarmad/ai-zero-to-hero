


def divisibleOf5(n) :
    
    if n%5 == 0 :
        return True
    else :
        return False
    
listOf5 = [5 , 10 , 15 ,19 , 5] 
print(list(filter(divisibleOf5 , listOf5)))