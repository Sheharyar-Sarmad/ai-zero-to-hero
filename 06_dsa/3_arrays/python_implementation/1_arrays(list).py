
# Before practicing this you should know intermediate level of python.

# Empty Array(list)

# arr = []

# Initialize Array(list) with type hint in python

# arr: list[int] = [1,2,3,4,5] # This list[int] means that the dtype of variable arr
# will be list and inside it the variables will be only dtypes of int(integers, like 1,2,3)

# Creating a list of a given size and filling it with zero

# size: int = len(arr)
# arr: list[int] = [0] * size

# List comprehension to fill with the squares roots till 10

# val: int = int(input("Enter a number: "))
# arr: list[int] = [val**2 for val in range(1,val)] # Order of n

# # Accessing Elements

# arr: list[int] = [10,20,30,40,50]
# print(arr[0]) # Print the 0th index element of the list arr
# print(arr[:2]) # Print the element from 0th index till 2nd
# print(arr[1:3]) # Print the element from 1st index till 3rd
# print(arr[2:]) # Print the element from 2nd index till end, that : means select till the end
# All are O(1) time complexity

# Inserting Element

# arr.append(60) -- add 60 at end of the list, no need to shift any other index so O(1)
# arr.append(2,60) -- insert at second and its O(n) because the next indexes might need to shift
# arr.extend([70,80]) -- at 70 and 80 atlast, O(k) where k is the number of added elements

# Deleting Element

# arr.remove(25) -- removes the first 25, O(n)
# arr.pop() -- removes the last element, O(1)
# arr.pop(2) -- remove the second indexes element and also return, O(n)
# del arr[2] -- same as arr.pop(2) but it didnt return anythin
# arr.clear() -- this will remove all the element from the list, O(n)

# Traversing and Iterating

# Its universally proven that iteration can never be O(1), because you have to look every element one by one
# in a collection even tough there's a hashmap and we will also it as well

# This is more dsa style and its always O(n)

# for i in range(len(arr)):
#     print(arr[i])

# This is advance pythonic way where you will directly can access the each value of the Array(list)

# for value in arr:
#     print(value)

# In enumerate(list_name) you can get both index and value

# for idx,val in enumerate(arr):
#     print(idx, val)

# Using in and index

# for i in arr:
#     print(f"{i} found at index", arr.index(30))

# Updating Element
# arr[2] = 20

# Sorting and Reversing

# arr.sort()             -- # in-place ascending
# arr.sort(reverse=True) -- # in-place descending
# arr.reverse()          -- # in-place reverse order

# Python also has sorted() which returns a new list.

# Multidimensional Arrays(list of list)

# martix: list[list[int]] = [
#     [1,2,3,],
#     [4,5,6],
#     [7,8,9]
# ]

# Accessing Element of row index 1 and column index 2

# print(matrix[1][2]) # 6 answer, this go to 1st indexed row and get its 2 indexed element

# Iterate over row and column

# O(r*c)
# for row in matrix:
#     for value in row:
#         print(value,end=" ")
#     print()