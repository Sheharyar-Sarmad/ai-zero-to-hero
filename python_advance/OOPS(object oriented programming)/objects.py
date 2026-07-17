class Factory :
    # There are two types of things in class attributes and methods
    a = 12 # attribute
    
    def hello(self) : # method
        print('Hello how are you!')
        
    print("hello how are you i am getting initialized!")

obj = Factory() # this is an object now

print(obj.a) # now obj variable is an instance of class Factory and obj can access all the things like Factory can do

# You can create objects as much as you need
obj2 = Factory()
obj3 = Factory()
obj4 = Factory() 
# and so on... 

# Important point: each objec will have the same power every object can access any attribute or method of a class.
 
obj.hello()