
# Basic Factory project using "Multi Level Inheritance": 

def starter():
    print("\nWelcome to the program\nIf you want to quite the program just type 'exit' to quite")
    
starter()

class Factory:
    def __init__(self , material: str , zips: int) -> None:
         self.material = material
         self.zips = zips
    
    @property
    def show(self): 
        class_name = self.__class__.__name__
        print(f"\nThis is from class {class_name}")
        print(f"\nYour object details are:\nmaterial: {self.material}\nzips: {self.zips}")

class BhopalFactory(Factory):
    def __init__(self , material: str , zips: int , color: str) -> None:
        super().__init__(material , zips)
        self.color = color
    
    @property
    def show(self): 
        class_name = self.__class__.__name__
        print(f"\nThis is from class {class_name}")
        print(f"\nYour object details are:\nmaterial: {self.material}\nzips: {self.zips}\ncolor: {self.color}")
        
class PuneFactory(BhopalFactory): 
    def __init__(self , material: str , zips: int , color: str , pockets: int) -> None:
        super().__init__(material , zips , color)
        self.pockets = pockets
    
    @property
    def show(self): 
        class_name = self.__class__.__name__
        print(f"\nThis is from class {class_name}")
        print(f"\nYour object details are:\nmaterial: {self.material}\nzips: {self.zips}\ncolor: {self.color}\npockets: {self.pockets}")

def get_input(prompt, input_type=str):
    """Helper function to get input with exit option"""
    while True:
        value = input(f"\n{prompt} (or 'exit' to quit): \n")
        if value.lower() == "exit":
            return None
        if input_type == int:
            try:
                return int(value)
            except ValueError:
                print(" Please enter a valid number!")
                continue
        return value

# Main loop
while True:
    material = get_input("Enter the material name")
    if material is None:
        break
    
    zips = get_input("Enter the number of zips", int)
    if zips is None:
        break
    
    color = get_input("Enter the color name")
    if color is None:
        break
    
    pockets = get_input("Enter the number of pockets", int)
    if pockets is None:
        break
    
    # Process data
    objFactory = Factory(material, zips)
    objFactory.show
    
    objBhopal = BhopalFactory(material, zips, color)
    objBhopal.show
    
    objPune = PuneFactory(material, zips, color, pockets)
    objPune.show

print("\nThanks for using our program!\nDeveloped by Sheharyar Sarmad\n")