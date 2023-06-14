# Pythonn data types Collection
# list
# tuple
# dict
# set

# list
# Indexed
# Multiple and duplicate
# ordered
# Mutable insert() update() append() delete() remove() pop() extend() sab garna milne

l = ["Apple","Ball","Cat","Dog"]
l1 = [1,2,3,4,5,6]
print(type(l))
print(type(l1))

l = list()
l1 = []


l = ["Apple","Banana","Cat","Dog","Elephant","Fish","Goat"]
print(l[0])
print(l[0:4])
print(l[0:7:3])


l = [1,2,3,4,5,6,7,7,6,7,6]
print(l)

# + *
a = [1,2,3,4,5]
b = [6,7]
c = a + b
print(c)

a = [6,7]
print(a*2)

# loop in list
a = ["Apple","Banana","Cat","Dog","Elephant","Fish","Goat"]
for i in l:
    print(i)

# range loop in list
a = ["Apple","Banana","Cat","Dog","Elephant","Fish","Goat"]
l = len(a)
print(l)
for i in range(l):
    print(a[i])

a = ["Apple","Banana","Cat","Dog","ELephant","Fish","Goat"]
if "Apple" in a:
    print("Yes")
    print(a.count("Apple"))
else:
    print("No")


# for input
# append() insert() extend()
# for delete
# del remove() pop()

a = []
a.append("Apple")
a.append("Ball")
print(a)

l=[]
n = int(input("Enter n = "))
for i in range(n):
    x = input("Enter x = ")    #ani integer ko lagi chae     x = int(input("Enter x ="))
    l.append(x)
print(l)

l = [1,2,3,4,5,7,6]
print("The maximum value = ",max(l))
print("The minimum value = ",min(l))
l.sort()
print(l)
l.reverse()
print(l)

a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"]    #special character is given first priority, numbers second and small letters are last while sorting.
a.sort()
print(a)

# insert()
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"] 
a.insert(0,"cat")              #insert garda agadhi input gareko index maa gayerw input gareko character gayerw basxa
print(a)

#euta list ko paxadi arko list lai extend garna: Use Extend.
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"] 
b = [1,2,3,4]
a.extend(b)
print(a)

# update
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"] 
a[3:4] = ["ball","cat"]        #0 matra gare list bhitra ni list nei aauxa
print(a)


# delete (index ko aadhar maa)
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"] 
del a[0:8:2]                     #del a[___] bhitra j index hunxa tey index ko value delete hunxa
print(a)

# index navayi value to aadhar maa delete garna chae remove use garne
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"]
a.remove("Cat")
print(a)

#multiple chha vane kasari remove garne:
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple","Ball",".apple","Ball"]
c = a.count("Ball")
for i in range(c):
    a.remove("Ball")
print(a)

#pop() {Yesma pani index tha hunuparxa}
a = ["Ball","Cat","Apple","Ant","Bat","apple","1apple",".apple"]
a.pop(0)
# b = a.pop(0)    # euta variable dekhi arko variable maa lyayerw rakhna chae yesto garna milxa
print(a)


# list inside list
l = [[1,2,3,4],
    [4,5,6,7],
    [8,9,0]]
print(type(l))

# list inside list
l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(type(l))

print(l[0])
print(l[2][1])

# To create list inside list by asking value to the user

info = []
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter the name = ")
    age = int(input("Enter age = "))
    add = input("Enter address = ")
    data = [name,age,add]
    info.append(data)
print(info)


l = [["Ram",90,"Kathmandu"], ["Shyam",34,"Bhaktapur"], ["Hari",45,"Lalitpur"]]
del l[0][0]
print(l)
 
l = [["Ram",90,"Kathmandu"], ["Shyam",34,"Bhaktapur"]]
l.append(['Hari',34,'Lalitpur'])
print(l)

l = [["Ram",90,"Kathmandu"], ["Shyam",34,"Bhaktapur"]]
l.insert(0,['Hari',34,"Lalitpur"])
print(l)