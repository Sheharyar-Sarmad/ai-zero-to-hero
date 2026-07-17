

# A constructor is a special method that is automatically called when an object is created. Its main purpose is to initialize the object's attributes (variables) and prepare it for use. In Python, the constructor is the __init__() method, which is executed automatically whenever a new object of a class is created. It usually takes self as its first parameter (which refers to the current object) and can accept additional parameters to assign initial values to the object's attributes.

class Factory :
    def __init__(self , material , zips , pockets) :
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
    def show(self) :
        print(f"Your objects details are materials: {self.material}, zips: {self.zips} , pockets: {self.pockets}")

reebok = Factory("leather" , 3 , 2)
campus = Factory("nylon" , 3 , 2)

reebok.show()
campus.show()