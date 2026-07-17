
lOfInt = [1,2,3,4,5,6,7,8,9,10]

countEven = 0
countOdd = 0



for digit in lOfInt :
    if isinstance(digit , int) :
        if digit % 2 == 0 :
            countEven += 1
        else :
            countOdd += 1
            
            
print(countEven , countOdd)