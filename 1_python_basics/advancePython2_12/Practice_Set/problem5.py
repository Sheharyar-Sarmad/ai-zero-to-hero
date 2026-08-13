

# # My logic:

# from functools import reduce

# l = [1 ,3 ,5 ,23, 21, 5342 , 23]

# maximumFunction = lambda a,b : a if a > b else b 

# maximum = reduce(maximumFunction , l)
# print(maximum)

# # Harry bhaoya logic:

# l = [111 , 2 , 65 , 53 , 635 , 65 , 74 ,45  , 55]

# def greater(a , b) :
#     if a > b :
#         return a
#     return b

# print(reduce(greater , l))