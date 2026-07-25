# for loop
# syntax
# for variable in sequence:
#     statement(s)

animals = ["cat", "dog", "rabbit", "tiger"]
for animal in animals:
    print(animal)
    
for color in ["red", "green", "blue"]:
    print(color)
    
for ch in "Manish":
    print(ch)       # M, a, n, i, s, h
    
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)      # 1 to 10

for num in range(1, 11):
    print(num)      # 1 to 10

for a in [1, 8]:
    print(a)      # 1 and 8
    
for a in range(1, 9, 1):
    print(a)      # 1 to 8 with step 1      -- 1, 2, 3, 4, 5, 6, 7, 8

for a in range(1, 9, 2):
    print(a)      # 1 to 8 with step 2    -- 1, 3, 5, 7

for a in range(8, 0, -1):
    print(a)      # 8 to 1 with step -1    -- 8, 7, 6, 5, 4, 3, 2, 1

for a in range(8, 0, -2):
    print(a)      # 8 to 1 with step -2    -- 8, 6, 4, 2
    
for num in range(1, 501):
    print(num)      # 1 to 500
    
# break statement
for num in range(1, 11):
    if num == 5:
        break
    print(num)      # 1, 2, 3, 4

for animal in ["cat", "dog", "rabbit", "tiger"]:
    if animal == "rabbit":
        break
    print(animal)   # cat, dog
    

# continue statement
for num in range(1, 11):
    if num == 5:
        continue
    print(num)      # 1, 2, 3, 4, 6, 7, 8, 9, 10
    
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if num == 5:
        continue
    print(num)      # 1, 2, 3, 4, 6, 7, 8, 9, 10
    

