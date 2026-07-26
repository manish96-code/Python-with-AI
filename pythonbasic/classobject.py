class ClassName:
    x = 40
    def hello(self):
        return "Hello"

obj = ClassName()
print(obj.x)    # 40
print(obj.hello())     # Hello 


class Employee:
    salary = 0
    
    def setSalary(self, salary):
        self.salary = salary
        
    def getSalary(self):
        return self.salary
    
emp = Employee()
emp.setSalary(10000)
print(emp.getSalary())     # 10000


# constructor 
class Employee:
    def __init__(self, salary):
        self.salary = salary
        
    def getSalary(self):
        print(self.salary)
        
emp1 = Employee(10000)
emp1.getSalary()    # 10000

emp2 = Employee(20000)
emp2.getSalary()    # 20000



# inheritance
class Student:
    def __init__(self, marks):
        self.marks = marks
        
    def getMarks(self):
        print(self.marks)
       
        
class Result(Student):
    def getStudentMarks(self):
        print("Student marks :", self.marks) 
        
std = Result(85)
std.getStudentMarks()

        
        
print("-------------")
class Tv:
    def __init__(self, brand = "Samsung", p = 10000, s = 32):
        self.vol = 0
        self.brand = brand
        self.price = p
        self.size = s

    def volUp(self):
        if self.vol < 10:
            self.vol += 1
        
    def volDown(self):
        if self.vol > 0:
            self.vol -= 1
        
# tv1 = Tv("LG", 45000, 32)
# tv1.volUp()
# tv1.volUp()
# tv1.volUp()
# print(tv1.vol)

class BrandedTv(Tv):
    def setBrand(self, brand):
        self.brand = brand
        
    def __init__(self, brand="Samsung", p=10000, s=32):
        super().__init__(brand, p, s)

sony = BrandedTv("sony", 45000, 38)
sony.volUp()
sony.volUp()
sony.volUp()
print(sony.vol)     # 3
sony.volDown()
print(sony.brand)    # sony
print(sony.price)    # 45000
print(sony.size)     # 38
sony.volDown()
sony.volDown()
sony.volDown()
sony.volDown()
sony.volDown()
print(sony.vol)     # 2
