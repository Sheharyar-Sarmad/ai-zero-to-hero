


def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("Hello i am decorator!")
        function(*args, **kwargs)

    return wrapper
#
# @mydecorator
# def helloworld():
#     print("Hello World!")

# mydecorator(helloworld)() # this is not the good pythonic way of doing it, theres one more versatile way
# of doing it.

# helloworld()

# Theres an error in @mydecorator as well now see whats that

@mydecorator
def hello(person):
    print(f"Hello {person}!")


hello("Sheharyar") # This will now give the error because wrapper takes 0 argument but given 1 overall
# we can add a single argument in wrapper function but we will not do it because its not the preferred way
# and also the main thing is we want our function decorator to be clickable for all the fuctions thats
# why add *args and **kwargs as an arguments in wrapper and also function argument