

l = [12 , 12 , 1242 ,13423]

# This is the simple version of doing this: 

# index = 0
# for i in l :
#     print(f"The item at index({index}) and the value is {i}")
#     index += 1

# This is the enumurate method(version) of doing this and this is more convenient and mostly used in industry as well:

for index , item in enumerate(l) :
    print(f"The item at index({index}) and the value is {item}")

