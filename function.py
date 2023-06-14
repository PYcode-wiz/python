# function
# pre-defined function
# user defined function

# pre-defined funciton
# print() input() int() float() str() bool() list() tuple() dict()

# def <function>():                 Defining
#     <operations>

# <function>()              Call

def hello():
    print("Hello World!")
hello()

def cal():
    l = int(input("Enter l = "))        #local variable
    b = int(input("Enter b = "))     
    a = l*b
    print(a)
cal()

# # function ko scope bahira define vayeko lai global variable which can be used both in and out of the function
# # local variable chae funtion ko scope bhitra matra define hunxa so use pani function bhitra matra hunxa

def hello(x):               #parameter
    print(x)
hello("Hello World")        #argument


l = int(input("Enter l = "))        
b = int(input("Enter b = ")) 
def cal(x,y):           # x,y parameter
    a = x*y
    print(a)
cal(l,b)                #l,b argument

l = int(input("Enter l = "))        
b = int(input("Enter b = ")) 
h = int(input("Enter h = "))
def cal(x,y,z):           
    a = x*y
    v = a*z
    print(a)
    print(v)
cal(l,b,h) 

def language(lan = "Python"):
    print(lan)

language("C")
language("C++")
language("Java")
language("Ruby")
language()

# return type 
def hello():
    return "Hello World!"
print(hello())


def cal():
    l = int(input("Enter l = "))
    b = int(input("Enter b = "))
    a = l*b
    return a
area = cal()
print(area)
h = int(input("Enter h = "))
volume = area*h
print(volume)

def cal():
    l = int(input("Enter l = "))
    b = int(input("Enter b = "))
    h = int(input("Enter h = "))
    a = l*b
    v = a*h
    return a,v
area, volume = cal()
print(area)
print(volume)

# area of rectangle
def area(x,y):
    return x*y
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Area of rectangle is",area(l,b))

# recursive function:
def hello():
    print("What's up?")
    a = input("Enter \"more\" for more printing: \n")
    if a == "more":
        hello()
hello()

# maths:
import math as m
print(m.pi)

print(m.factorial(5))

print(m.sin(m.pi/2))

print(m.cos(m.pi/2))

print(m.tan(m.pi/2))

# lambda function
# lambda <arguments>:<operation>

x = lambda a: a**2
print(x(5))

x = lambda l,b: l*b
print(x(2,5))

# filtering 
a = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2==0, a)))

a = [1,2,3,4,5,6,7,8,9,9,7,5,6,8,3,5,4,6,7,8,]
print(list(filter(lambda x: x>5, a)))

# mapping
a = [1,2,3,4,5]
print(list(map(lambda x: x*2,a)))

a = ["Apple","Ball","cat","dog","fish","Zebra"]
list(map(lambda x: x.lower(),a))

a = [1,2,3,4,5]
list(map(lambda x: 0.5*x + 10,a))