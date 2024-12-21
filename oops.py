class student:
    "this is class"
    x=10
    y=20
    def add(p,q):
        return p+q
    def __init__(self):    #it is a reference variable that holds address of current class of current object.
        print("constructor called")
        print(id(self))
obj=student()
print(id(obj))
# print(dir(student))
# print(dir(obj))
print(obj.__doc__)  #for calling class description or string


#another example
class school:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print(id(self))
obj1=school('mms','indore')
print(id(obj1))
obj2= school("sss",'bhopal')
print(id(obj2))
print(obj1.name)
print(obj2.name)


#constructor= it is a special type of method and () is responsible for calling the constructor, it can be 
#explicitly called


#variables=
#instance var.= object dependent var.
#class variable= not dependent on object
#local var.= declare on a method or function 
#instance var.= where we can declare instance var.
class student:
    def __init__(self,name,age):
        self.name=name   # declare inside constructor
        self.age=age
        print(self.name)
        print(self.age)     #calling of variable

    def add(self,school):
        self.school=school     # declare inside method
        print(self.name)     #calling
        print(self.age)

    def show(self):
        print(self.name)
        print(self.age)
        print(self.marks)      #calling
        print(self.school)
obj=student('kratika',22)
obj.marks=[10,20,30,40,50]    # declare outside of the class
print(obj.name)     #calling
print(obj.age)
obj.add("technocrats")
obj.show()


#class var. /static var.
class student:
    school="technocrats"     #declare
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.school_city="bhopal"    #declare
        print(student.school)      #calling
    def add(self):
        student.school_code=201    #declare
        print(student.school_city)    #calling
obj=student('kratika',22)
student.school_principle="indore"     #declare 
print(student.school_city)      #calling
print(student.school_principle)


#local var.
x=50
class student:
    x=10
    def new():
        print(x)
    def new1():
        global x
        print(x)
        x=5
        print(x)
obj=student
print(x)
obj.new()
obj.new1()
print(x)


#methods=
#instance method
class a:
    def new(self):
        print('hello')
    def new1(self):
        self.new()
obj=a()    #it is compulsory to use () of calling the method in instance method
obj.new()
obj.new1()


#class method= used to modified class variable or static variable
# @classmethod word used
class book:
    price=150
    def __init__(self,author,year):
        self.x=author
        self.y=year
    def show(self):
        print(self.x)
        print(self.y)
        print(book.price)
    @classmethod
    def update(cls,price):
        cls.price=price
obj=book('kratika',2002)
obj.show()
obj.update(300)
obj.show()


#static method
class book:
    price=150
    def __init__(self,author,year):
        self.x=author
        self.y=year
    def show(self):
        print(self.x)
        print(self.y)
        print(book.price)
    @staticmethod
    def update():
        print('hello everyone')
obj=book('kratika',2002)
obj.show()
book.update()