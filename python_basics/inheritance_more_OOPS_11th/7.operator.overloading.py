# ==============================
# OPERATOR OVERLOADING CHEATSHEET
# ==============================

# Note: 
# the double underscore(__(method)__) is called as dunder methods in python.

# Arithmetic Operators
# p1 + p2      → __add__(self, other)
# p1 - p2      → __sub__(self, other)
# p1 * p2      → __mul__(self, other)
# p1 / p2      → __truediv__(self, other)
# p1 // p2     → __floordiv__(self, other)
# p1 % p2      → __mod__(self, other)
# p1 ** p2     → __pow__(self, other)

# Reverse Operators (when left object can't handle operation)
# p1 + p2      → __radd__(self, other)
# p1 - p2      → __rsub__(self, other)
# p1 * p2      → __rmul__(self, other)
# p1 / p2      → __rtruediv__(self, other)

# Comparison Operators
# p1 == p2     → __eq__(self, other)
# p1 != p2     → __ne__(self, other)
# p1 > p2      → __gt__(self, other)
# p1 < p2      → __lt__(self, other)
# p1 >= p2     → __ge__(self, other)
# p1 <= p2     → __le__(self, other)

# String / Representation
# print(obj)   → __str__(self)
# repr(obj)    → __repr__(self)

# Length & Container
# len(obj)           → __len__(self)
# obj[index]         → __getitem__(self, key)
# obj[index] = value → __setitem__(self, key, value)

# Special Methods
# Constructor        → __init__(self)
# Destructor         → __del__(self)

# NOTE:
# These methods allow custom classes to behave like
# built-in types (numbers, strings, lists, etc.)

class Number:
    def __init__(self , n) :
        self.n = n
    def __add__(self , num) :
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)