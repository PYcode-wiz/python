a = 'Hello World'
b = "Hello World"
c = '''Hello World'''
print(type(a))
print(type(b))
print(type(c)) 

a = "Hello World"
for i in a:
    print(i, end="")

a = "Hello World"
print(a[0])
print(a[0:5])
print(a[0:10:2])


a  = "Hello World"
print(a[-1:-12:-1])

a = "Hello World"
a[::-1]

a = "Hello World"
a[-1:-6:-1]

#string formatting
name = input("Enter name.\n")
add = input("Enter address.\n")
age = int(input("Enter age.\n"))
# info = "Hello I am "+name+". I am from "+add+". I am "+str(age)
# print(info)

info = f"Hello World I am {name}. I am from {add}. I am {age}."
print(info)

n = int(input("Enter n = "))
s = str()
for  i in range(n):
    name = input("Enter name = ")
    phone = int(input("Enter phone = "))
    s = s + f"{name} {phone}\n"

name = input("Enter name")
a = "Ram Shyam Hari Sita Gita Nabin Ramesh"
if name in a:
    print("Yes there is.")
    print(a.count(name))
else:
    print("No")

a = "Ram Shyam Hari Sita Gita Nabin Ramesh"
print(a.lower())             
print(a.upper())             
print(a)          #immutable i.e unchangeable

a = "Ram Shyam Hari Sita Gita Ramesh Nabin"
a = a.replace('Shyam','')
print(a)          #mutable i.e changeable





# To reverse any string.
w = input("Enter any text.\n")
a = w[::-1]
print("The reverse of",w,"is",a)



# To know wheather a given word is palindrome or not.
w = input("Enter any word.\n")
a = w[::-1]
if w == a:
    print("Your given word is palindrome.")
else:
    print("Your given word is not palindrome.")