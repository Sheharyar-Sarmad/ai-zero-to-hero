


# list = ["an" , "ayan" , "Harry"]

# def removeValues(l , word) :
#     n = []
#     for item in l :
#         if not(item == word) :
#             n.append(item.strip(word))
#     return n

# print(removeValues(list , "an"))


names = ["Sheharyar" , "Harry" , "Carry" , "Merry" , "Kerry"]

def removeAlphabets(list , word) :
    newList = [] # empty list:
    for item in list :
        if not(item == word) :
            newList.append(item.replace(word , ""))
    return newList

print(removeAlphabets(names , "er"))