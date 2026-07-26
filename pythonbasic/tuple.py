my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)     # (1, 2, 3, 4, 5)
# my_tuple[0] = 10     # error, tuple is immutable
print(my_tuple[0])     # 1
print(my_tuple[4])     # 5
print(my_tuple[-2])     # 4
print(my_tuple[2:5])     # (3, 4, 5)
print(len(my_tuple))    # 5

my_tuple2 = tuple((1, 2, 3, 4, 5))
print(my_tuple2)     # (1, 2, 3, 4, 5)
print(type(my_tuple2))     # tuple

my_tuple3 = tuple([1, 2, 3, 4, 5])
print(my_tuple3)     # (1, 2, 3, 4, 5)
print(type(my_tuple3))     #tuple


num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for x in num:
    print(x)     # 1 2 3 4 5 6 7 8 9
    
