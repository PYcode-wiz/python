# OOP = Object Oriented Programming.

# Class, Object, Method

# class: class is a blueprint for the object.
class Python:
    pass

# Object: object(instance) is an initialization of a class.
obj = Python()

# Method: method are the function defined inside the body of a class used to define the behaviour of an object.


# 
class Hello:                            #class
    @staticmethod
    def hello():                        #method
        print("Hello World")

obj = Hello()                           #object
obj.hello()

# 
class Hello:                           
    def hello(self):                   
        print("Hello World")

obj = Hello()                          
obj.hello()

# static method:
class Cal:
   @staticmethod
   def cal():
       l = 10
       b = 2
       a = l*b
       print(a)
obj = Cal()
obj.cal() 

# self method:
class Cal:
   def cal(self):
       l = 10
       b = 2
       a = l*b
       print(a)
obj = Cal()
obj.cal() 

# 
class Cal:
   def cal(self,l,b):
       a = l*b
       print(a)

l = 10
b = 2
obj = Cal()
obj.cal(l,b) 

# 
class Cal:
   def __init__(self,l,b):
       self.l = l
       self.b = b
   def cal(self):
       a = self.l * self.b
       print(a)

l = 10
b = 2
obj = Cal(l,b)
obj.cal() 

# same as above but this program also finds the volume:
class Cal:
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h
    def area(self):
        a = self.l * self.b
        print(a)
    def volume(self):
        v = self.l * self.b * self.h
        print(v)
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))
obj = Cal(l,b,h)
obj.area() 
obj.volume()

# 
class Info:
    def __init__(self):
        self.name = input('Enter name: ')
        self.age = int(input("Enter age: "))
        self.add = input("Enter address: ")
    def info(self):
        print(f"Hello World I am {self.name}. I am {self.age} years old. I am from {self.add}.")
obj = Info()
obj.info()
print(obj.name)
print(obj.age)
print(obj.add)

# 
class Info:
    def __init__(self):
        self.name = input('Enter name: ')
        self.age = int(input("Enter age: "))
    def info(self,add):
        print(f"Hello World I am {self.name}. I am {self.age} years old. I am from {add}.")
obj = Info()
obj.info("Kathmandu")
print(obj.name)
print(obj.age)

# inheritance: capability of one class to derive or inherit the properties from some another class.

# class A:
#     <methods>
#     <methods>
# class B(A):
#     <method1>
#     <method2>
# obj = B()

# 
class A:
    def __init__(self):
        self.name = "Satyam"
        self.age = 15
        self.add = "Kathmandu"
class B(A):
    def info(self):
        print(f"Hello World. I am {self.name}. I am from {self.add}. I am {self.age} years old.")
obj = B()
obj.info()

# single class maa init method
class A:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add
class B(A):
    def info(self):
        print(f"Hello World. I am {self.name}. I am from {self.add}. I am {self.age} years old.")
obj = B("Satyam","15","Kathmandu")
obj.info()

# dubei class maa init
class A:
    def __init__(self,age,add):
        self.age = age
        self.add = add
class B(A):
    def __init__(self,name,age,add):
        self.name = name
        A.__init__(self,age,add)
    def info(self):
        print(f"Hello World. I am {self.name}. I am from {self.add}. I am {self.age} years old.")
obj = B("Satyam","15","Kathmandu")
obj.info()

# syntax of multi-level inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass
obj = C()

# multi-level inheritance:
class A:
    def __init__(self,add):
        self.add = add
class B(A):
    def __init__(self,age,add):
        self.age = age
        A.__init__(self,add)
class C(B):
    def __init__(self,name,age,add):
        self.name = name
        B.__init__(self,age,add)
    def info(self):
        print(f"Hello World. I am {self.name}. I am from {self.add}. I am {self.age} years old.")
obj = C("Satyam","15","Kathmandu")
obj.info()

# multiple inheritance:
class A:
    def __init__(self,add):
        self.add = add
class B:
    def __init__(self,age):
        self.age = age
class C(A,B):
    def __init__(self,name,age,add):
        self.name = name
        B.__init__(self,age)
        A.__init__(self,add)
    def info(self):
        print(f"Hello World.. My name is {self.name}. I am from {self.add}. I am {self.age} years old.")
obj = C("Satyam","15","Kathmandu")
obj.info()

# public members:
class Info:
    def __init__(self):
        self.name = "Ram"
        self.age = 34
        self.add = "Kathmandu"
obj = Info()
print(obj.name)
print(obj.age)
print(obj.add)

# protected members:
class Info:
    def __init__(self):
        self._name = "Ram"
        self._age = 34
        self._add = "Kathmandu"
obj = Info()
print(obj._name)
print(obj._age)
print(obj._add)

# private members:
class Info:
    def __init__(self):
        self.__name = "Ram"
        self.__age = 34
        self.__add = "Kathmandu"
obj = Info()
print(obj.__name)
print(obj.__age)
print(obj.__add)

# 
class A:
    def __init__(self):
        self.name = "Satyam"
        self._age = 15
        self.__add = "Kathmandu"
    def infos(self):
        print(f"Hello World. I am {self.name}. I am {self._age} years old. I am from {self.__add}")
class B(A):
    def info(self):
        print(f"Hello World. I am {self.name}. I am {self._age} years old.")
obj = B()
obj.info()
obj.infos()

# multi inheritance
class A:
    def __init__(self,add):
        self.add = add
class B(A):
    def __init__(self,age,add):
        self.age = age
        A.__init__(self,add)
class C(B):
    def __init__(self,name,age,add):
        self.name = name
        B.__init__(self,age,add)
    def info(self):
        print(f"Hello World. I am {self.name}. I am from {self.add}. I am {self.age} years old.")
obj = C("Satyam","15","Kathmandu")
obj.info()


# multiple inheritance:
class A:
    def __init__(self):
        self.__add = "Kathmandu"
    def add(self):
        return self.__add
class B:
    def __init__(self):
        self._age = 22
class C(A,B):
    def __init__(self):
        self.name = "Ram"
        B.__init__(self)
        A.__init__(self)
    def info(self):
        add = A.add(self)
        print(f"Hello World. My name is {self.name}. I am from {add}. I am {self._age} years old.")
obj = C()
obj.info()

# private lai access garne method:
class Info:
    def __init__(self):
        self.__name = "Ram"
        self.__age = 34
        self.__add = "Kathmandu"
obj = Info()
print(obj._Info__name)
print(obj._Info__age)
print(obj._Info__add)