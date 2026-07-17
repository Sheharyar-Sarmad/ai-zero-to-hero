
# Encapsulation

# Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit (class), while restricting direct access to the internal details of an object. It's about hiding the internal state and requiring all interaction to be performed through an object's methods.


# Example:

# class Factory:
#     __a = "pune"
    
#     def show(self):
#         print(Factory.__a)
        
# class Bhopal(Factory):
#     def show(self):
#         # print(super().__a) # double underscore before teh attribute or method name declaration make that attribute or method private mean that no one can access them outside of class
        
# obj = Factory()
# obj.show()