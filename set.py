# set
# - no indexing
# - Multiple but no duplicate value
# - mutable
# - non-ordered 
# - mutable

s = {1,2,3,4,5,6,7}
print(type(s))

s = set()


# s = {1,2,{3,4,5,6,7}
# print(s[0])


s = {1,2,3,4,5,6,7,7}
print(s)

s = {"Apple","Ball","Cat","Dog","Fish"}
print(s)

# add() remove()
# no + *
# no concat 

# update 
a = {"Apple","Ball","Cat","Dog","Fish"}
b = {1,2,3,4,5,6,7}
a.update(b)
print(a)

# add
s = set()
s.add("Apple")
s.add("Ball")
print(s)

# remove
a = {"Apple","Ball","Cat","Dog","Fish"}
a.remove('Apple')
print(a)

# conversion of list to set then again set to list:
a = [1,2,3,3,3,1,2,5,7,3,2,8,9,7,3,4,5,6,2,6,8,4,6,7]
b = list(set(a))
print(b)

# union(), intersection(), difference()
U = {"xyz","Ram","Steve","Hari","Shyam","Nabin","Sita","Ram","Hari","Shyam","Gita","Ramesh","Shiva"}
apple = {"Ram","Steve","Hari","Shyam","Nabin","Sita"}
ms = {"Ram","Hari","Shyam","Gita","Ramesh","Shiva"}
i = apple.intersection(ms)
print(i)

u = apple.union(ms)
print(u)

d = apple.difference(ms)    # = apple maa matra kaam garne hru. And if ms maa matra kaam garne thapauna xa vane = d = ms.difference(apple)
print(d)


print(U - apple.union(ms))

a = {[1,2,3]}
print(a)    #output= error

# set inside set, list inside set, dict inside set not possible