#program to set key and value by the user

#creating empty dictionary
'''dic={}
a='yes'
while a=='yes':
    key=input("Enter your key value")
    value=input("Enter your value for the key")
    if value.isdigit()==True:
        value=int(value)
    else:
        value=value
#inserting entered key and value to the dictionary
    dic[key]=value

    a=input('type yes to add more')
print(dic)


#program to verify the email entered by the user
#importing regular expression
import re
import sys
reinput='yes'

email=input("Enter your email")
pattern='^.*@.*$'
var=re.match(pattern,email)
if var:
    print("Email matched")
else:
    sys.exit("INVALID EMAIL")

#implementing inheritance
class Human:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def display(self):
        print("Your name is ",self.name)
        print("Your age is ",self.age)
        print("your gender is ",self.gender)
class Nepali(Human):
    def __init__(self,nationality,Human):
        self.name=Human.name
        self.age=Human.age
        self.gender=Human.gender
        self.nationality=nationality
    def details(self):
        print(" your name is",self.name)
        print("Your age is",self.age)
        print(" Your Gender is ",self.gender)
class City(Nepali):
    def __init__(self,cityname,address,Nepali,Human):
        self.name=Human.name
        self.age=Human.age
        self.gender=Human.gender
        self.nationality=Nepali.nationality
        self.cityname=cityname
        self.address=address
    def show(self):
        print(" your name is",self.name)
        print("Your age is",self.age)
        print(" Your Gender is ",self.gender)
        print("Your city name is ",self.cityname)
        print("your address is ",self.address)
obj1=Human('Prachi','Female',22)
obj2=Nepali("NEPALI",obj1)
obj3=City("Itahari","Jutebikas",obj2,obj1)
obj1.display()
obj2.details()
obj3.show()'''

#student management program using class
import sys
class StudentId:
    def __init__(self,id,name,faculty,grade,rollNum):
        self.id=id
        self.name=name
        self.faculty=faculty
        self.grade=grade
        self.rollNum=rollNum
    def display(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Faculty: ",self.faculty)
        print("Grade: ",self.grade)
        print("Roll NUmber: ",self.rollNum)
class StudentFee(StudentId):
    def __init__(self,totalfee,paidfee,due,StudentId):
        self.name=StudentId.name
        self.faculty=StudentId.faculty
        self.grade = StudentId.grade
        self.totalfee=totalfee
        self.paidfee=paidfee
        self.due=due
    def details(self):
        print("Name: ",self.name)
        print("Faculty: ", self.faculty)
        print("Grade: ",self.grade)
        print("Total Course Fee: Rs.",self.totalfee)
        print("Total paid fee: Rs.",self.paidfee)
        print("TOtal amount to be paid: Rs.",self.due)
#creating object for the class StudentId
select='y'
while select=='y':
    print("Select Your Choice: ")
    print("   1. To view Student personal Details")
    print("   2. To view student fee Details")

    get=int(input("Enter you choice "))

    if get==1:
        obj1=StudentId(200123,'Prachi Sapkota','BSC. CSIT','Bachelor',8316)
        obj1.display()
#creating object for the class StudentFee
    elif get==2:
        obj2=StudentFee(400000,280000,120000,obj1)
        obj2.details()
    else:
        sys.exit("Invalid Input ")
    select=input("Enter 'y' to continue")