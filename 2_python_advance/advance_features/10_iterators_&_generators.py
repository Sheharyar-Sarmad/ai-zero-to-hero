


def numbers():
    for i in range(1, 6):
        yield i

for n in numbers():
    print(n)

numbers()

print(next(numbers()))