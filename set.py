my_set = {1, 2, 3, 4, 5, 4}
print(my_set)     # {1, 2, 3, 4, 5}
print(type(my_set))     # set

# print(my_set[0])     # error

my_set.add(6)
print(my_set)     # {1, 2, 3, 4, 5, 6}

my_set.update([7, 8, 9])
print(my_set)     # {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set.discard(8)
print(my_set)     # {1, 2, 3, 4, 5, 6, 7, 9}


# set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
print(set1 | set2)     # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection
print(set1 & set2)     # {4, 5}

# difference
print(set1 - set2)     # {1, 2, 3}

# symmetric difference
print(set1 ^ set2)     # {1, 2, 3, 6, 7, 8}


# empty set
empty_set = set()
print(empty_set)     # set()
print(type(empty_set))     # set
