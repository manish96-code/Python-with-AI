def greet():
    print("Hello")

greet()


# function with argument
def greet(name):
    print("Hello", name)

greet("Manish")      # Hello Manish
greet("Aman")       # Hello Aman


def sum(num1, num2):
    print(num1 + num2)

sum(10, 20)  # 30
sum(30, 50)  # 80
# sum(30, 50)/2    # error


def sum(num1, num2):
    return num1 + num2

print(sum(10, 20))  # 30
print(sum(30, 50)/2)  # 40


# default arguments
def greet(name = "Manish"):
    print("Hello", name)

greet()          #Hello Manish
greet("Aman")      #Hello Aman


def sum(num1, num2 = 20):
    print(num1 + num2)
    
sum(10)         #30
sum(10, 30)     #40


# arbitary value
def sum(*num):
    result = 0
    for i in num:
        result += i
    return result

print(sum(1, 2, 3, 4, 5))         # 15
print(sum(1, 2, 3))              # 6
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


# keyword argument
def person(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

person("Manish", 20, "Patna")       # name=Manish, age=20, city=Patna
person(22, "Aman", "Kolkata")       # name=22, age=Aman, city=Kolkata
person(name = "Manish", age = 20, city = "Patna")      # name=Manish, age=20, city=Patna   
person(age = 20, name = "Manish", city = "Patna")      # name=Manish, age=20, city=Patna


# built in function
print(len("Hello"))       # 5
print(max(1, 2, 3, 4, 5))    # 5
print(min(1, 2, 3, 4, 5))    # 1
# print(sum([1, 2, 3, 4, 5]))    # 15


# local variable
def greet():
    x = 10
    print(x)

greet()    #10
# print(x)    # error


# global variable
a = 20
def greet():
    print(a)

greet()    #20
print(a)   #20


# nonlocal variable
def outer():
    a = 10
    def inner():
        nonlocal a
        a = 20
        print("Inner : ", a)
    inner()
    print("Outer : ", a)
outer()


# global keyword
num = 30
def greet():
    global num
    num = 10
    print(num)

greet()    #10
print(num)   #10