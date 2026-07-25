try:
    print(5 / 0)
except:
    print("Error : cannot divide by zero")


try:
    num = [5, 10, 15]
    print(num[2])
    print(5 / 0)
except IndexError:
    print("Error : index out of range")
except ZeroDivisionError:
    print("Error : cannot divide by zero")


try:
    print(5 / 0)
except:
    print("Error : cannot divide by zero")
else:
    print("No error")
finally:
    print("This is finally block")