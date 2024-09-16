class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
     print(self.__acc_pass)

acc1 = Account(12345, 444444)
print(acc1.acc_no)
print(acc1.reset_pass)
class person:
    __name = "Anounomous"
    def __hello(self):
        print("hello dear!")

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())

#Inheritence method
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")
    
class toyotacar(Car):
    def __init__(self, name):
        self.name = name
c1 = toyotacar("fortuner")
c2 = toyotacar("prius")
print(c1.stop())

#Class method 
class person:
    name = "Anounomus"
    @classmethod 
    def change_name(self, name):
         self.name = name

p1 = person()
p1.change_name("Annas")
print(p1.name)
print(person.name)

#property method
class student:
    def __init__(self, phy, chem, bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
    @property
    def percentage(self):
        return ((self.phy + self.chem + self.bio)/ 3), "%"



stu1 = student(78,69,98)
print(stu1.percentage)
stu1.phy = 98
print(stu1.percentage)

#polymorphism
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def shownumber(self):
        print(self.real, "i +", self.imaginary, "j")

    def __add__(self, num2):
        newreal = self.real +num2.real
        newimaginary = self.imaginary + num2.imaginary
        return Complex(newreal + newimaginary)
num1 = Complex(3,6)
num1.shownumber()
num2 = Complex(2,3)
num2.shownumber()
num3 = num1 + num2
num3.shownumber()
