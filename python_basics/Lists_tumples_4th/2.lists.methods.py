# ==============================
# FUNCTION & ADVANCED LIST METHODS
# ==============================

# Example list:
# Lists in Python can store multiple data types.
# Lists are mutable (can be changed).
# They use index starting from 0.

# friends = ["Apple", "Orange", 5, 340.6, False, "Aakash", "Rohan"]

# ------------------------------
# 1. append()
# Adds ONE element at the end of the list.
# Modifies the original list.
# friends.append('Sheharyar')
# print(friends[7])

# ------------------------------
# l1 = [1, 1, 4, 34, 62, 2, 6, 1, 1, 1, 1]

# ------------------------------
# 2. sort()
# Sorts the list in ascending order by default.
# Changes the original list (in-place).
# For descending order use: l1.sort(reverse=True)

# l1.sort()
# print(l1)

# ------------------------------
# 3. reverse()
# Reverses the current order of the list.
# Does NOT sort.
# Changes the original list.
# Returns None.

# l1.reverse()
# print(l1)

# ------------------------------
# 4. insert(index, value)
# Inserts an element at a specific index.
# Shifts existing elements to the right.

# l1.insert(3, "KAISE HAI")
# changeType = str(l1[4])
# typeOfChangeType = type(changeType)
# print(l1, typeOfChangeType)

# ------------------------------
# 5. pop(index)
# Removes element at a specific index.
# Returns the removed value.
# If no index is given, removes last element.

# l1.pop(3)
# print(l1)

# value = l1.pop(3)
# print(value)   # prints removed value
# print(l1)

# ------------------------------
# 6. remove(value)
# Removes the FIRST matching value from the list.
# Does NOT return anything.
# Raises error if value not found.

# removeVariable = l1.remove(34)
# print(l1)

# ------------------------------
# 7. extend(iterable)
# Adds multiple elements at the end of the list.
# Used to merge lists.

# l1.extend([4,5,6,3])
# print(l1)

# ------------------------------
# 8. clear()
# Removes all elements from the list.
# Makes it empty: []

# l1.clear()
# print(l1)

# ------------------------------
# 9. index(value)
# Returns the index of the first occurrence of value.
# Raises error if value not found.

# indexOflist = l1.index(2)
# print(indexOflist)

# ------------------------------
# 10. count(value)
# Returns how many times a value appears in the list.

# countof1inlist = l1.count(1)
# print(countof1inlist)