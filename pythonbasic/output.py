# print(object = seperator = end = file = flush =)

print("Hello, World")          # Hello, World!
print('Hello, World')          # Hello, World
print("Hello", "World")        # Hello World
print("Hello", "World", 2026)       # Hello World 2026
print("Hello" + " " + "World")      # Hello World
print("Hello", "World", 20, sep="-")          # Hello-World-20
print("Hello", "World", 20, sep=" and ")          # Hello and World and 20
print("Hello", "World", 20, sep=" | ")          # Hello | World | 20
print("Hello", "World", 20, sep=" ---- ")          # Hello ---- World ---- 20
print("Hello", "World", 20, sep=" ")          # Hello  World  20

print("Hello", end=" ")          # Hello    , end=" " means that after printing "Hello", it will print a space instead of a newline
print("World")                   # World



# Output formatting
name = "Manish"
msg = "Good Morning"

# .format() method
print("Hello {}, and your message is {}".format(name, msg))   # Hello Manish, and your message is Good Morning
print("Hello {0}, and your message is {1}".format(name, msg))   # Hello Manish, and your message is Good Morning
print("Hello {1}, and your message is {0}".format(name, msg))   # Hello Good Morning, and your message is Manish

# regular expression
print(f"Hello {name}, and your message is {msg}")   # Hello Manish, and your message is Good Morning

# c style formatting
print("Hello %s, and your message is %s" % (name, msg))   # Hello Manish, and your message is Good Morning