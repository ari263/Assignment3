a = input('Enter a number: ')
a = int(a)


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


print("Factorial of", a, "is:", fact(a))
