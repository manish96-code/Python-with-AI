# Data types are the types of data that can be stored in a variable.


# Single value data types
x = 5
y = 3.14
z = "Hello, World!"
print(type(x))      # int
print(type(y))      # float
print(type(z))      # str

print(x == y)     # False
print(x > y)      # True

a = None
print(a)          # None


# Multiple value data types
animals = ["Dog", "Cat", "Rabbit"]
print(type(animals))   # list
print(animals[0])   # Dog
print(animals[1])   # Cat
print(animals[2])   # Rabbit

animals2 = ("Dog", "Cat", "Rabbit")
print(type(animals2))   # tuple

data = {1,2,3,4,5}
print(type(data))   # set 

person = {"name": "John", "age": 30, "city": "Purnea"}
print(type(person))   # dictionary / dict
print(person["name"])   # John
print(person["age"])    # 30
print(person["city"])   # Purnea


name = "Manish Kumar"
print(type(name))    # str