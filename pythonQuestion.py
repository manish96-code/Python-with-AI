# num = input("Enter a list of numbers separated by spaces: ").split()

# if len(num) == len(set(num)):
#     print("All numbers are unique")
# else:
#     print("Duplicate numbers found")




# Write a Python program to count the number of vowels in a string entered by the user.
# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in string:
#     if char in vowels:
#         count += 1
# print("Number of vowels in the string:", count)




# def display(*numbers):
#     print(numbers)

# display(10, 20, 30)
# display(1, 2, 3, 4, 5)



# num = input("Enter a list of numbers separated by spaces: ")
# print(set(num))
# print(len(num))
# print(len(set(num)))



# import module1
# module1.greet()


# text = "Python"

# print(text[1:4])    # yth
# print(text[:3])     # Pyt
# print(text[3:])     # hon
# print(text[-2:])    # on
# print(text[2:5])    # tho
# print(text[:])      # Python



# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()



# name = "Manish"

# print(name[1:4])    # ani
# print(name[:3])     # Man
# print(name[3:])     # ish
# print(name[-2:])    # sh
# print(name[2:5])    # nis
# print(name[:])      # Manish
# print(name[1:5:2])  # ai
# print(name[::2])    # Mns
# print(name[::-1])   # hsinaM


# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(num[1:4])     # [2, 3, 4]
# print(num[:3])      # [1, 2, 3]
# print(num[3:])      # [4, 5, 6, 7, 8, 9, 10]
# print(num[-2:])     # [9, 10]
# print(num[2:7:2])   # [3, 5, 7]
# print(num[::3])     # [1, 4, 7, 10]


# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)

# # Output:
# # True



# a = [1, 2, 3]
# b = a
# print(a is b)

# # Output:
# # True


# print("Hello")
# print(len("Python"))

# # Output:
# # Hello
# # 6



# print(len(("Hello\n")))


# print("Hello\nWorld")



# def greet():
#     print("Hello Manish")

# greet()

# # Output:
# # Hello Manish


# code
# numbers = [12, 45, 7, 89, 23, 56, 34, 10, 78, 5]

# print("List:", numbers)
# print("Maximum Value:", max(numbers))
# print("Minimum Value:", min(numbers))
# print("Sum of Elements:", sum(numbers))
# print("Ascending Order:", sorted(numbers))

# # Output:
# # List: [12, 45, 7, 89, 23, 56, 34, 10, 78, 5]
# # Maximum Value: 89
# # Minimum Value: 5
# # Sum of Elements: 367
# # Ascending Order: [5, 7, 10, 12, 23, 34, 45, 56, 78, 89]



# # code
# import re

# text = "Python is a popular programming language."
# result = re.search("Python", text)

# print(result)

# # Output:
# # <re.Match object; span=(0, 6), match='Python'>





# import re

# text = "Python is easy"
# result = re.match("Python", text)

# print(result)

# # Output:
# # <re.Match object; span=(0, 6), match='Python'>




# import re

# text = "cat bat cat mat"

# result = re.findall("cat", text)

# print(result)

# # Output:
# # ['cat', 'cat']


# import numpy as np

# arr = np.array([10, 20, 30, 40])

# print(arr)

# # Output:
# # [10 20 30 40]


# -----------------------------------------

# import numpy as np

# arr = np.array([10, 20, 30, 40])
# print(arr * 2)

# # Output:
# # [20 40 60 80]



# import numpy as np

# arr = np.array([23, 45, 67, 89, 12])
# print(arr)

# # Output:
# # [23 45 67 89 12]



# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# # Output:
# # [[1 2 3]
# #  [4 5 6]]


# import numpy as np

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr)

# # Output:
# # [[[1 2]
# #   [3 4]]
# #  [[5 6]
# #   [7 8]]]


# import numpy as np

# arr = np.array([44, 55, 35, 22, 11])
# print(arr[2])

# # Output:
# # 35



# import numpy as np

# arr = np.array([90, 39, 78, 56, 12])
# print(arr[1:3])

# # Output:
# # [39 78]



# import numpy as np

# arr = np.array([7, 14, 21, 28, 35])
# new_arr = arr.copy()

# print("Original array:", arr)        # [ 7 14 21 28 35]
# print("Copied array:", new_arr)      # [ 7 14 21 28 35]



# import numpy as np

# arr = np.array([9, 4, 6])
# new_arr = arr.view()

# print("Original array:", arr)        # [9 4 6]
# print("View of the array:", new_arr)  # [9 4 6]



# import numpy as np

# arr = np.array([[11, 42, 63], [14, 35, 46]])
# print(arr.shape)

# # Output:
# # (2, 3)



# import numpy as np

# arr = np.array([6, 2, 6, 1, 9, 6])
# new_arr = arr.reshape(2, 3)
# print(new_arr)

# # Output:
# # [[6 2 6]
# #  [1 9 6]]


# import numpy as np

# arr1 = np.array([11, 45, 33])
# arr2 = np.array([90, 54, 56])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# # Output:
# # [11 45 33 90 54 56]



# import numpy as np

# arr = np.array([16, 32, 48, 64, 80, 96])
# new_arr = np.array_split(arr, 3)
# print(new_arr)

# # # Output:
# # # [array([16, 32]), array([48, 64]), array([80, 96])]



# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])
# new_arr = arr[arr > 25]
# print(new_arr)

# # Output:
# # [30 40 50]


# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = np.array([10, 20, 30, 40, 50])
# sns.histplot(data)
# plt.show()



# number = input("Enter a number: ")
# digit = input("Enter the digit to count: ")

# count = 0

# for i in number:
#     if i == digit:
#         count += 1

# print("The digit", digit, "appears", count, "times.")

# # Output:
# # Enter a number: 834797324973294723
# # Enter the digit to count: 4
# # The digit 4 appears 3 times.



# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))

# if month == 2:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print("Number of days = 29")
#     else:
#         print("Number of days = 28")

# elif month in [4, 6, 9, 11]:
#     print("Number of days = 30")

# else:
#     print("Number of days = 31")


# Output:
# Enter year: 2020
# Enter month (1-12): 2
# Number of days = 29


# ........................................

# import numpy as np
# x = np.random.randint(1, 10)
# print(x)


# import numpy as np
# x = np.random.rand(5)
# print(x)



# import numpy as np
# x = np.random.choice([10, 20, 30, 40])
# print(x)


# import numpy as np
# x=np.random.poisson(lam=5,size=10)
# print(x)


# import numpy as np
# x=np.random.uniform(1,10,10)
# print(x)



# import numpy as np
# x=np.random.logistic(loc=0,scale=1,size=10)
# print(x)



# import numpy as np
# x=np.random.multinomial(20,[1/6]*6)
# print(x)


# import numpy as np
# x=np.random.exponential(scale=2,size=10)
# print(x)


# import numpy as np
# x=np.random.chisquare(df=2,size=10)
# print(x)
