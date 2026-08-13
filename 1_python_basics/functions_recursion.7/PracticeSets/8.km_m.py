def km_m(n) :
    if(n == 0) :
        return 'Invalid number 0 is not allowed'
    else:
        return n * 1000
        
num = float(input("Enter your number: "))
print(f"{num} km = {km_m(num)} meter")