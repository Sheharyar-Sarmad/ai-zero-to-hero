

myList = [ 2 , 3 , 9 , 8 , 5 , 6 ]

# This is messy way and in this method we have to right more code :

# squaredList = []

# for item in myList :
#     squaredList.append(item*item)

# print(squaredList)

# This method is more convinient and called as list comprehension. and also used in industry as well:

squaredList = [i*i for i in myList]
print(squaredList)