# Empty list
empty_list = []
list1 = []


# string list
names = ["Manish", "Ravi", "Suresh", "Anil", "Sunil"]
print(names)       # ['Manish', 'Ravi', 'Suresh', 'Anil', 'Sunil']
print(names[0])     # Manish
print(names[1])     # Ravi
print(names[2])     # Suresh
print(names[-1])    # Sunil
print(names[-2])    # Anil


# mixed list
mixed_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(mixed_list)     # [1, 'Hello', 3.14, True, [1, 2, 3]]
print(mixed_list[0])     # 1
print(mixed_list[1])     # Hello
print(mixed_list[2])     # 3.14
print(mixed_list[3])     # True
print(mixed_list[4])     # [1, 2, 3]
print(mixed_list[4][0])     # 1
print(mixed_list[4][1])     # 2
print(mixed_list[4][2])     # 3
print(mixed_list[-1])      # [1, 2, 3]
print(mixed_list[-1][2])    # 3
print(mixed_list[-1][-1])    # 3
print(mixed_list[-1][-2])    # 2
print(mixed_list[-1][-3])    # 1


# nested list
nested_list = [1, [2, 3], [4, 5, 6], 7]
print(nested_list[0])     # 1
print(nested_list[1])     # [2, 3]
print(nested_list[1][0])     # 2
print(nested_list[1][1])     # 3
print(nested_list[2][2])     # 6



name = "Manish"
print(name[0])     # M
print(name[1])     # a
print(name[2])     # n
print(name[-1])    # h

name = ["Manish"]
print(name[0][0])     # M
print(name[0][1])     # a
print(name[0][2])     # n
print(name[0][-1])    # h

num = [1,2,3,4,[1,2,3,4,5,[12,13]]]
print(num[-1][-1][-1])     # 13



# Slicing
names = ["Manish", "Sanu", "Raj", "Rohan", "Mohan"]
print(names[1:4])     # ['Sanu', 'Raj', 'Rohan']
print(names[:3])      # ['Manish', 'Sanu', 'Raj']
print(names[3:5])     # ['Rohan', 'Mohan']
print(names[2:])      # ['Raj', 'Rohan', 'Mohan']
print(names[:])       # ['Manish', 'Sanu', 'Raj', 'Rohan', 'Mohan']
print(names[-3:-1])   # ['Raj', 'Rohan']
print(names[-2:])     # ['Rohan', 'Mohan']
print(names[:-2])     # ['Manish', 'Sanu', 'Raj']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])   # [3, 4, 5, 6, 7]
print(numbers[:3])    # [1, 2, 3]
print(numbers[5:])    # [6, 7, 8, 9]
print(numbers[10:20])  # []
print(numbers[3:3])   # []
print(numbers[3:2])   # []


# add elements to list
names = ["Manish", "Sanu", "Raj"]
names.append("Rupesh")
print(names)     # ['Manish', 'Sanu', 'Raj', 'Rupesh']

names.insert(1, "Rohan")
print(names)     # ['Manish', 'Rohan', 'Sanu', 'Raj', 'Rupesh']

names.extend(["Mohan", "Sakshi", "Priya"])
print(names)     # ['Manish', 'Rohan', 'Sanu', 'Raj', 'Rupesh', 'Mohan', 'Sakshi', 'Priya']


# remove elements from list
names = ["Manish", "Rohan", "Sanu", "Raj", "Rupesh"]
names.remove("Sanu")
print(names)     # ['Manish', 'Rohan', 'Raj', 'Rupesh']



# del
x = [1, 2, 3, 4, 5, 6, 7, 8]
print(x)    # [1, 2, 3, 4, 5, 6, 7, 8]
del x[2]    # remove element at index-2
print(x)    # [1, 2, 4, 5, 6, 7, 8]

del x[1:4]
print(x)    # [1, 6, 7, 8]


# pop
name = ["Abhi", "Shivam", "Rosy", "Priya", "Sakshi"]
print(name.pop())     # Sakshi
print(name)           # ['Abhi', 'Shivam', 'Rosy', 'Priya']

print(name.pop())  # Shivam
print(name)         # ['Abhi', 'Rosy', 'Priya']

print(len(x))    # 4


# iterate list through for loop 
names = ["Manish", "Rohan", "Sanu", "Raj", "Rupesh"]
for name in names:
    print(name)


# list comprehension
num = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in num]
print(doubled)     # [2, 4, 6, 8, 10]

triple = [n * 3 for n in num]
print(triple)     # [3, 6, 9, 12, 15]

add2 = [n + 2 for n in num]
print(add2)        # [3, 4, 5, 6, 7]


