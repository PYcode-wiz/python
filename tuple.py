# indexed
# ordered
# multiple and duplicate values
# immutable
t = ()
a = ("Apple",)
b = ("Ball",)
t = t+a+b
print(t)

# tuple matra banaune:
t = ()
n = int(input("Enter n = "))
for i in range (n):
    a = input("Enter the value = ")
    b = input("Enter the value = ")
    t = t+(a,)+(b,)
print(t)

# tuple maa changes garne method:
a = ("Apple","Ball","Cat")
b = list(a)   #yo line maa tuple lai list banako so that changes garna milos
del b[0]
a = tuple(b)   #yesma chae feri list lai tuple banako
print(a)

#tuple inside tuple
l = (("Ram",45,"Kathmandu"),
     ("Shyam",34,"Bhaktapur"),
     ("Hari",23,"Lalitpur"))

print(l[0])