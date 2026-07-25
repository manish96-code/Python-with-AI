# unary operators
a = 5
print(-a)    # -5
print(+a)    # 5

# binary operators
x = 10
y = 5
print(x + y)    # 15
print(x * y)    # 50


# Arithmetic operators
a = 10
b = 3
print(a + b)      # 13
print(a - b)      # 7
print(a * b)      # 30
print(a / b)      # 3.333...
print(a // b)     # 3       floor division
print(a % b)      # 1
print(a ** b)     # 1000


# Assignment operators
x = 5
x += 3    # x = x + 3
print(x)  # 8
x -= 2    # x = x - 2
print(x)  # 6
x *= 4    # x = x * 4
print(x)  # 24
x /= 6    # x = x / 6
print(x)  # 4.0
x //= 2   # x = x // 2
print(x)  # 2.0
x %= 2    # x = x % 2
print(x)  # 0.0
x **= 3   # x = x ** 3
print(x)  # 0.0


# Comparison operators
a = 10
b = 5
print(a == b)     # False
print(a != b)     # True
print(a > b)      # True
print(a < b)      # False
print(a >= b)     # True
print(a <= b)     # False


# Logical Operators
x = True
y = False
print(x and y)   # False
print(x or y)   # True
print(not x)    # False
print((x and y) or (not y))   # False

a = 5
b = 10
c = 15
print(a < b and b > 0)  # True
print(a > b or b > 0)   # True
print(a < c and c > 0)  # True
print(a > c or c < a)   # False

print(True and False)  # False
print(True or False)   # True
print(not True)        # False
print(not False)       # True


# Bitwise Operators
a = 5      # 0101
b = 3      # 0011

# Bitwise AND
print(a & b)   # (0001) = 1

# Bitwise OR
print(a | b)    # (0111) = 7

# Bitwise XOR
print(a ^ b)    # (0110) = 6   if bits are same result is 0, if different result is 1

# Bitwise NOT
print(~a)       # -6

# Bitwise Left Shift
print(a << 1)   # (1010) = 10
print(a << 2)   # (10100) = 20
print(a << 3)   # (101000) = 40
print(a << 4)   # (1010000) = 80

# Bitwise Right Shift
print(a >> 1)   # (0010) = 2
print(a >> 2)   # (0001) = 1
print(a >> 3)   # (0000) = 0
print(a >> 4)   # (0000) = 0
