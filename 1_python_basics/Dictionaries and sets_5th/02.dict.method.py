
# Some advance features and function of dictionaries used commonly in python programming examples are given as under here:

# d = {} # this creates an empty dictionary
# marks = {
#     "Harry" : 100,
#     "Subham" : 56 , 
#     "Rohan" : 23 ,
#     0 : "Harry"
# }

# print(marks[0]) 
# this will not go on marks 0 index it will find the 0 key value and then returns "Harry" as a output

# print(marks.items())
# this will give you the dic.. items in tumples form of each key and value  like that dict_items([('Harry', 100), ('Subham', 56), ('Rohan', 23), (0, 'Harry')])

# print(marks.keys())
# this will give you the Key values of dictionaries only not their values only key variables like that dict_keys(['Harry', 'Subham', 'Rohan', 0])

# print(marks.values())
 # this will returns the values of all the keys in a dictionaries

# marks.update({ "Harry": 99 , "Renuka" : 100 }) 
# this will also add the new value and key if you add the key which is not existed in the dictionary yet
# print(marks) 

#  whats the difference in both of these
# print(marks.get("Harry2")) 
# both have no keys in dic this will give you None as output
# print(marks["Harry2"])
# It also dont have any key like this in dic but this will return an error as an output
# print(marks.clear())
# print(marks.pop('Harry'))