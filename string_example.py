str1 = "Hello World"
print(str1[0])      # H
print(str1[2])      # l
print(str1[7])      # o
print(str1[-1])     # d
print(str1[-5])     # W    
print(str1[0:4])    # Hell 
print(str1[6:11])   # World
print(str1[-5:-1])  # Worl
print(str1[:5])     # Hello

str1 = "Hello"
str2 = "Hello"

# comparison of strings
print(str1 == str2)  # True
print(str1 != str2)  # False

# concatenation of strings
print(str1 + str2)  # HelloWorld
print(str1 + " " + str2)  # Hello World

# iteration
for i in str1:
    print(i)      # H e l l o

# in operator (membership)
print("H" in str1)  # True
print("Z" not in str1)  # True


# Methods of strings
print(str1.upper())  # HELLO
print(str1.lower())  # hello
print(str1.capitalize())  # Hello
print(str1.partition("l"))  # ('He', 'l', 'lo')
print(str1.strip("H"))  # ello
print(str1.replace("H", "Z"))  # Zello
print(str1.find("H"))  # 0
print(str1.index("H"))  # 0
print(str1.count("H"))  # 1
print(str1.startswith("H"))  # True
print(str1.endswith("l"))  # False
print(str1.split(" "))  # ['Hello']


# Escape sequence
print("Hello\nWorld")  # Hello
                    # World
print("Hello\tWorld")  # Hello    World
print("\"Hello World\"") # "Hello World"
print("'Hello World'") # 'Hello World'
print("Hello \\ World") # Hello \ World
print('"Hello World"') # "Hello World"
