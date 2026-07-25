# Variables are containers for storing data values.

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 5
print(x)
print(type(x))      # int

x = "Hello World"
print(x)
print(type(x))      # str

x = str(10)
print(x)    
print(type(x))      # str


name = "Manish"
age = 30
print(name)
print(age)


# One value to multiple variables
x = y = z = 20
print(x)
print(y)
print(z)


# Multiple Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# Output Variables
x = "Python"
print(x)