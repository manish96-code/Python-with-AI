print("10" * 2)



x = [1, 2, 3]
y = x
y.append(4)
print(x)

print(9 ** 0.5)

print(abs(-7))

print(round(2.6))
print(round(2.5))
print(round(2.9))
print(round(3.5))

print(5 == 5.0)




print(round(3.5))
name = "Manish"
print(name[0])

print("------------------------------------")

print(int("1010", 2))
print(int(2))
print(int("1010"))

x = [1, 2, 3]
x.pop()
print(x)

x = [1, 2, 3]
print(x.index(2))


print(len({'a': 1, 'b': 2, 'a': 3}))

result = [x for x in range(10) if x % 2 != 0]
print(result)

print([1, 2, 3].pop(0))


vals = [10, 20]
vals.append([30, 40])
print(vals)
print(len(vals))

items = ['apple', 'banana', 'cherry']
print(items.pop())
print(items)

colors = ['red', 'blue', 'green']
colors.extend('white')
print(colors)


print("-----------------------------------")
items = [1,2,3,4,5]
items.extend([8,9])
print(items)
print(len(items))



print("-----------------------------------")

# Prime number
# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")




print("-----------------------------------")

# ATM pin
# pin = 1234
# current_balance = 10000
# for i in range(3):
#     input_pin = int(input("Enter your pin: "))
#     if input_pin == pin:
#         print("Correct pin")
#         withdraw_amount = int(input("Enter amount to withdraw: "))
#         if withdraw_amount <= current_balance:
#             print("Transaction successful")
#             current_balance = current_balance - withdraw_amount
#             print("Current balance: ", current_balance)
#         else:
#             print("Insufficient balance")
#             print("Current balance: ", current_balance)
#         break
#     else:
#         print("Incorrect pin")
# else:
#     print("Card blocked")


print("-----------------------------------")


a = 53
b = 87
c = 99
    
# if a > b:
#     print(a, "is greater")
# else:
#     print(b, "is greater")
    
    
if a > b and a > c:
    print(a, "is greater")
elif b > a and b > c:
    print(b, "is greater")       
else:
    print(c, "is greater")
    
print(max(99, 12, 656))




print("-----------------------------------")

colors = ['red', 'blue', 'green']
colors.extend('white')
print(colors)
print(len(colors))



for i in "Manish":
    print(i)
    
name = "Manish"
print(name[3])
print(name[5])
print(name[-1])
print(len(name) - 1)

print("-----------------------------------")

# num = int(input("Enter any number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

print("-----------------------------------")
# prime number
# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")
    
    
    
print("-----------------------------------")
# prime number 1 to 100
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        

print("-----------------------------------")

name = ["raj", "rohan", "rupesh"]
del name[1:3]
print(name)     # ['raj']

print("-----------------------------------")

name = "Manish"
sno = 1
# for i in range(100):
#     print(f"{sno}. {name}")
#     sno += 1



print(10 == "10")     # False
print(10 == 10.0)     # True

print("Hello".replace("l", "x"))

set1 = {7, 8, 9, 4, "sa",  4, "rerew"}
print(set1)

my_set = {1, 2, 3, 4, 5, 4}
print(my_set)     # {1, 2, 3, 4, 5}
print(type(my_set))     # set
my_set.discard(8)
print(my_set)     # {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)     # {1, 2, 4, 5}


print("-----------------------------------")

# Prime number
# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")




# def fun(n):
#     count = 0
#     i = n
#     while i > 0:
#         for j in range(i):
#             count += 1
#         i //= 2
#     return count


print(bool(False))
print(bool())


print("-----------------------------------")


import pytz
from datetime import datetime

time1 = pytz.timezone("Asia/Kolkata")
date = datetime.now(time1)
print(date)

time2 = pytz.timezone("US/Pacific")
date = datetime.now(time2)
print(date)


print("\"Hello\"")


print(type(10))