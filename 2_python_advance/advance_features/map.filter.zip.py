
# The map() function applies a given function to every item in an iterable (like a list) and returns a map object (iterator).


# map(function, iterable)
# # OR
# map(function, iterable1, iterable2, ...)

a = [1,2,3,4,5]

result = map(lambda x : x**2 , a)
print(list(result))

# The filter() function creates an iterator that filters elements from an iterable based on a condition (function that returns True or False).

# filter(function, iterable)

even = filter(lambda x : x % 2 == 0 , a)
print(list(even))

morePractice = filter(lambda x: x > 1 and x < 5 , a)
print(list(morePractice))