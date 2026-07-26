x = 5
if x == 5:
    print("x is 5")
    
y = 10
if y > 0:
    print("y is positive")
else:
    print("y is negative")
    
    
# indentation
a = 20
# if a > 10:
# print("a is greater than 10")       # error



age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
    
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")



# Ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult


# Nested if-else statement
num = 15
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")




# even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
    

# largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")