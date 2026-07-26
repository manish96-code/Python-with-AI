str1 = "python"
for i in range(len(str1)-1, -1, -2):
    print(str1[i])
    
print(5 == "5")

print(bool(" "))

print(0 or 5)

print([1, 2, 3] * 0)



print("abc".find("fd"))


print(round(3.5))
print(round(2.5))


print("abc".find("d"))

print("Python"[::2])

x = [1, 2, 3]
x.append([4,5])
print(x)
print(len(x))


x = {1, 2, 3}
x.add(2)
print(x)


print(bool([0]))


print(6 or 0 or 5)
print(6 and 8 and 5)


print(bool("False"))

a={1,2,3,4}
b={3,4,5,6}

print(a|b)  # union
print(a&b)  # intersection
print(a-b)  # difference
print(a^b)  # symmetric difference

print(2 ** 3 ** 2)

print(bool(float("nan")))

x = [[1, 2]] * 3
x[0][0] = 99
print(x)



x = [1,2,3]
y = x
y.append(4)

print(x)


x = {}
print(type(x))


print([1, 2] is [1, 2])

print(bool(0))

