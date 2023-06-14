# WAP to detect if the number is prime or composite
# prime=2,3,5,7,11,13,17
# composite=4,6,8,9,10,12,14

# to create a pattern
for i in range(1,6):
     print(i*'*')


# For multiplication table using break:
n = int(input("Enter any number: "))
for i in range(1,12):
     if i == 11:
          break
     print(n,"x",i,"=",n*i)

# Addition of multiple number taken from users.
s = 0
i = 0
n = int(input("Enter n = "))
while i<n:
    x = int(input("Enter x = "))
    s = s + x
    i = i+1
print(s)

#  To reverse any string.
w = input("Enter any word.\n")
r = w[::-1]
print(r)

# To know wheather a given word is palindrome or not.
w = input("Enter any word.\n")
a = w[::-1]
if w == a:
    print("Your given word is palindrome.")
else:
    print("Your given word is not palindrome.")


# WAP to calculate factorial of 4! =1*2*3*4
# WAP to create a pattern.
# WAP to calculate grade of multiple students.




# WAP to create tuple inside tuple
# WAP to convert tuple inside tuple to list inside list



# WAP to create tuple inside tuple.
t = ()
l = list(t)
n = int(input("Enter n(please do not enter 0 or 1. Start from 2) = "))
for i in range (n):
    name = input("Enter name. ")
    age = int(input("Enter age. "))
    add = input("Enter address. ")
    data = (name,age,add)
    l.append(data)
    t = tuple(l)
print(t)


# WAP to convert tuple inside tuple to list inside list.

l = (("Ram",15,"Kathmandu"),("Hari",16,"Lalitpur"))
t = list[l]
print(t)    #****


# WAP to create a matrix by taking row and column value from user and input data in it. {list ko qn}
row = int(input("Enter the number of rows. "))
columns = int(input("Enter the number of columns. "))
matrix = [[int(input()) for c in range (columns)] for r in range(row)]
print(matrix)      #****


# WAP to add, update, delete in the following dict.
# d = {'Ram':[9867667654,9808778765], 'Shyam': [9867887654,9808778765]}

# for adding:
d = {'Ram':[9867667654,9808778765], 'Shyam': [9867887654,9808778765]}
n = int(input("Enter n = "))
for i in range(n):
        name = input("Enter name. ")        
        phone1 = int(input("Enter phone no. "))
        phone2 = int(input("Enter other phone no. "))
        d[name] = [phone1,phone2]
print(d)

# for updating:
d = {'Ram':[9867667654,9808778765], 'Shyam': [9867887654,9808778765]}
n = int(input("Enter n = "))
for i in range(n):
        name = input("Enter the name. ")
        phone1 = int(input("Enter the new ncell phone no. "))
        phone2 = int(input("Enter the new ntc phone no. "))
        d[name] = [phone1,phone2]
print(d)

# for deleting:
d = {'Ram':[9867667654,9808778765], 'Shyam': [9867887654,9808778765]}
del d[input("Enter the name you want to delete. ")]
print(d)



# WAP to add update delete in the following list.
l = [{'name':'Ram', 'age':34, 'add':'Kathmandu'},
     {'name':'Shyam', 'age':23, 'add':'Lalitpur'},
     {'name':'Ramesh', 'age':24, 'add':'Bhaktapur'}]

# for adding:
l = [{'name':'Ram', 'age':34, 'add':'Kathmandu'},
     {'name':'Shyam', 'age':23, 'add':'Lalitpur'},
     {'name':'Ramesh', 'age':24, 'add':'Bhaktapur'}]
n = int(input("Enter n: "))
for i in range(n):
     name = input("Enter name: ")
     age = int(input("Enter age: "))
     add = input("Enter address: ")
     info = {'name':name,'age':age,'add':add}
     l.append(info)
print(l)

# for deleting:
l = [{'name':'Ram', 'age':34, 'add':'Kathmandu'},
     {'name':'Shyam', 'age':23, 'add':'Lalitpur'},
     {'name':'Ramesh', 'age':24, 'add':'Bhaktapur'}]
del l[int(input("Enter index. "))]
print(l) 

# repeatition of word, number of times according to the user requirement:
n = int(input("Enter n = "))
a = input("Enter word. ")
for i in range(n):
    print(a)

# WAP to create grading system using funciton.



# WAP to create a basic calculator using function.
def add(x,y):
     return x+y
def subtract(x,y):
     return x-y
def multiply(x,y):
     return x*y
def divide(x,y):
     return x/y

a = int(input("Enter the first number. "))
b = int(input("Enter the second number. "))
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Enter your choice. (a/b/c/d) ")

if choice == "a":
     print("The sum of",a,"and",b,"is",add(a,b))
elif choice == "b":
     print("The difference of",a,"and",b,"is",subtract(a,b))
elif choice == "c":
     print("The product of",a,"and",b,"is",multiply(a,b))
elif choice == "d" and b != 0:
     print("The quotient of",a,"and",b,"is",divide(a,b))
elif choice == "d" and b == 0:
     print("The value of the second number cannot be zero.")
else:
     print("Invalid Operation.")


# one line calculator.
print(eval(f'{input()}'))


# OOP:

# WAP to print name, age, address using oop concept.
# single class init  method:
class A:
     def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add
class B(A):
     def info(self):
        print(f"Hello. I am {self.name}. I am {self.age} years old. I am from {self.add}.")
obj = B("Satyam","15","Kathmandu")
obj.info()

# MULTI-LEVEL INHERITANCE:
# double class init(value = user accordingly):
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class B(A):
    def __init__(self,name,age,add):
        self.add = add
        A.__init__(self,name,age)
    def info(self):
        print(f"Hello. I am {self.name}. I am {self.age} years old. I am from {self.add}.")
name = input("Enter your name: ")
age = input("Enter age: ")
add = input("Enter address: ")
obj = B(name,int(age),add)
obj.info()

# triple class init(value = user accordingly):
class A:
    def __init__(self,name):
        self.name = name
class B(A):
    def __init__(self,name,age):
        self.age = age
        A.__init__(self,name)
class C(B):
    def __init__(self,name,age,add):
        self.add = add
        B.__init__(self,name,age)
    def info(self):
        print(f"Hello. I am {self.name}. I am {self.age} years old. I am from {self.add}.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
add = input("Enter address: ")
obj = C(name,age,add)
obj.info()

# MULTIPLE INHERITANCE(value = user accordingly):
class A:
    def __init__(self,name):
        self.name = name
class B:
    def __init__(self,age):
        self.age = age
class C(A,B):
    def __init__(self,name,age,add):
        self.add = add
        A.__init__(self,name)
        B.__init__(self,age)
    def info(self):
        print(f"Hello. I am {self.name}. I am {self.age} years old. I am from {self.add}.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
add = input("Enter your address: ")
obj = C(name,age,add)
obj.info()

# perimeter area and volume:
# MULTI-LEVEL INHERITANCE:
class P:
     def __init__(self,l):
         self.l = l
class A(P):
     def __init__(self,l,b):
         self.b = b
         P.__init__(self,l)
class V(A):
     def __init__(self,l,b,h):
         self.h = h
         A.__init__(self,l,b)
     def info(self):
         print("The perimeter of rectangle with length",l,"and breadth",b,"is",peri)
         print("The area of rectangle with length",l,"and breadth",b,"is",area)
         print("The volume of recrangle with length",l,"breadth",b,"and height",h,"is",volume)
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
h = int(input("Enter the height: "))
peri = 2*(l+b)
area = l*b
volume = l*b*h
obj = V(l,b,h)
obj.info()

# MULTIPLE INHERITANCE: 
class P:
     def __init__(self,l):
         self.l = l
class A:
     def __init__(self,b):
         self.b = b
class V(P,A):
     def __init__(self,l,b,h):
          self.h = h
          P.__init__(self,l)
          A.__init__(self,b)
     def result(self):
          print("The perimeter of rectangle with length",l,"and breadth",b,"is",peri)
          print("The area of rectangle with length",l,"and breadth",b,"is",area)
          print("The volume of recrangle with length",l,"breadth",b,"and height",h,"is",volume)
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))
peri = 2*(l+b)
area = l*b
volume = l*b*h
obj = V(l,b,h)
obj.result()