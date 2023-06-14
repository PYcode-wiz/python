for i in range(5):
    print(i)

for i in range(5):
    print(i,"Hello World")    


for i in range(1,5):
    print(i,"Hello World")


for i in range(1,5,2):    #1,3
    print(i,"Hello World")


n = int(input("Enter n = "))
for i in range(1,11):
    print(i*n)


n = int(input("Enter n = "))
for i in range(1,11):
    print(n,"*",i,"=",i*n)


n = 5
for i in range(n):
    x = int(input("Enter x = "))
    print(x)


n = int(input("Enter n = "))
s = 0
for i in range(n):
    x = int(input("Enter x = "))
    s = s + x
print(s)


n = int(input("Enter n = "))
s = str()   #s = ""
for i in range(n):
    x = input("Enter x = ")
    s = s + x + "\n"
print(s)


# WAP to input name and phone no of users
n = int(input("Enter n = "))
s = str()   #s = ""
for i in range(n):
    name = input("Enter name = ")
    phone = int(input("Enter phone = "))
    s = s + name +" "+ str(phone) + "\n"
    
print(s)


a = "Python"
print(a)
for i in a:
    print(i,"Hello World")


a = "Python"
for i in a:
    print(i,end = ".")


a = "Hello World. I am Python. I am best."
for i in a:
    if i != ".":
        print(i,end = "")

a = "Hello World. I am Python. I am best."
for i in a:
    if i != " ":
        print(i,end = "")


a = "Hello World. I am Python. I am best."
for i in a:
    if i != " " and i != ".":
        print(i,end = "")

while True:
    print("Hello World")


a = 0
while a < 5:
    print(a,"Hello World")
    a = a+1


a = 1
while a < 5:
    print(a,"Hello World")
    a = a+1


a = 1
while a <= 5:
    print(a,"Hello World")
    a = a+2


a = 5
while a >= 0:
    print(a,"Hello World")
    a = a-1


i = 1
n = int(input("Enter n = "))
while i<=10:
    print(n,"*",i,"=",i*n)
    i = i+1


s = 0
i = 0
n = int(input("Enter n = "))
while i<n:
    x = int(input("Enter x = "))
    s = s + x
    i = i+1    
print(s)


# WAP to input name and phone no of users
i = 0
n = int(input("Enter n = "))
s = str()   #s = ""
while i<n:
    name = input("Enter name = ")
    phone = int(input("Enter phone = "))
    s = s + name +" "+ str(phone) + "\n"
    i = i+1
print(s)


#break statement

for i in range(20):
    if i == 5:
        break
    print (i)

# continue statement
for i in range(20):
    if i == 5:
        continue
    print (i)

#  break
a = "Hello World I am python. I am best."
for i in a:
    if i == ".":
        break
    print(i, end = "")
print(".")

# continue
a = "Hello World I am python. I am best."
for i in a:
    if i == ".":
        continue
    print(i, end = "")
print(".")

# while maa break
i = 0
while i <=10:
    if i == 5:
        break
    print(i)
    i = i+1


# while maa continue
i = 0
while i <=10:
     if i == 5:
         i = i+1
         continue
     print(i, end=" ")
     i = i+1