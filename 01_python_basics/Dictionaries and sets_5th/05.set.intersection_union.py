# 👉 Union = All unique elements from both sets combined
# 👉 Intersection = Only common elements between both sets

s1 = {1 , 45 , 6 , 78}
s2 = {7 , 8 , 1 , 78}

print(s1.union(s2))         
# Union → combines both sets and removes duplicates

print(s1.intersection(s2))  
# Intersection → gives only common elements (1 and 78)


a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
# issubset() → Checks:
# "Are ALL elements of a inside b?"
# If yes → True
# If even one element is missing → False


print(b.issuperset(a))
# issuperset() → Checks:
# "Does b contain ALL elements of a?"
# If yes → True
# If not → False

print(b.pop())