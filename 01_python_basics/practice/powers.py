


n = int(input("Enter your number"))


for i in range(1,11) : 
    print(n**i)
    
    
powers = [n ** i for i in range(1,11)]
print(powers)