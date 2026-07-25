def greet(x):
    if x <= 10:
        print(x)
        greet(x + 1)
    else:
        return 0

greet(1)


# sum of first n natural numbers
def sum(x):
    if x <= 10:
        return x + sum(x + 1)
    else:
        return 0

result = (sum(1))
print(result)


# factorial
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

result = (factorial(7))     # 5040
print(result)