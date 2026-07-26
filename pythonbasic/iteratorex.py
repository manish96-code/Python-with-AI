num = [1, 2, 3, 4, 5]

x = iter(num)
print(next(x))     # 1
print(next(x))     # 2
print(next(x))     # 3
print(next(x))     # 4
print(next(x))     # 5
# print(next(x))      # error


# using for loop

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in num:
    print(x)     # 1 2 3 4 5 6 7 8 9 10