n = 12345
sumOfN = 0

for eachn in str(n):        # Convert n to a string
    sumOfN += int(eachn)    # Convert each character back to int and add

print("Sum of digits:", sumOfN)