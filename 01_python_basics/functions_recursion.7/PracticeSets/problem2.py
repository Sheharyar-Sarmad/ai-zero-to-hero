import time


def f_to_c(f):
    return (f - 32) * 5 / 9


f = float(input("Enter temperature in Fahrenheit ° : "))
print("")

print(f"Converting {f} ° Fahrenheit into Celsius...")
print("")
time.sleep(1)

result = f_to_c(f)
print(f"{result:.3f} ° Celsius")

time.sleep(1)
print("")
print("Thanks for using, this programme is created by Sheharyar Sarmad")