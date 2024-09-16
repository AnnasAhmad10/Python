#if a constructor contains only (self) its called default constructor.
#parameterized constructor
class Car:
    def __init__(self,name):
        self.name = name
        print("Adding new car to  showroom..")

c1 = Car("BMW")
print(c1.name)
c2 = Car("toyota")
print(c2.name)

class Student():
    def __init__(self, subjectname, marks):
        self.subjectname = subjectname
        self.marks = marks
        
s1 = Student("phy", 70)                            #Exercise Question
print(s1.subjectname, s1.marks)
s2 = Student("chem", 80)
print(s2.subjectname, s1.marks)
s3 = Student("bio", 90)
print(s3.subjectname, s1.marks)

print("average marks =", (s1.marks + s2.marks +s3.marks)/3)
#different method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is:", sum/3)

s1 = Student("Ali", [50, 60, 70])
s1.avg()

s1.name = "farhan"
s1.avg()

#Banking system
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "has been debited from your account")
        print("Total Amount=", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "has been credited to your account")
        print("Total Amount=", self.get_balance())

    def get_balance(self):
     return self.balance

acc1 = Account(50000, 8908787)
acc1.credit(5000)
acc1.debit(2000)
acc1.credit(80000)

