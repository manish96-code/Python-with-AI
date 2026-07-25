name = input("Enter your name: ")
print("Your name is", name)
print("Your name is " + name)
print(f"Your name is {name}")
print("Your name is %s" % name)
print(name)


# Type conversion
# implicit type conversion
x = 5
y = 2.5
z = x + y   # z is a float
print(z)    # 7.5
print(type(z))  # float


# explicit type conversion
x = 5
y = 6.5
y = int(y)
print(x + y)    # 11
print(type(y))  # int


age = input("Enter your age: ")   # age is a string
print("Your age is", age)         # Your age is 25
print(type(age))              # string

age = int(input("Enter your age: "))   # age is converted to an integer
print("Your age is", age)         # Your age is 25
print(type(age))              # integer