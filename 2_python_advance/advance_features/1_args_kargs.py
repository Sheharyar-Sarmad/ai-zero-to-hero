

# args example
def addition(*args): # this *args creates a tuple. eg...(12,1,23,12,3)
    sum = 0
    
    for i in args:
        sum = sum + i 
    
    print(sum)
    
addition(12,231,213,12,3,123,21,3,21,3,213)


# Kwargs example
def kwargs_function(**kwargs): # this **kwargs creates dictionary. eg..{'a':1,'b':2,'c':3}
    print(kwargs)
    
kwargs_function(a=1,b=3,c=3)