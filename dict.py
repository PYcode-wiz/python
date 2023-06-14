# dictionary
# indexing
# ordered
# multiple and duplicate data
# mutable

d = {}
d = dict()
print(d)
print(type(d))


# d = {<key>:<value>, <key>:<value,...}

d = {'a':'Apple','b':'Ball','c':'Cat'}
print(d)
print(len(d))
print(d['a'])

d = {'a':'Apple','b':'Ball','c':'Cat','a':'apple'}
print(d)

# dict maa operator nei use hudeina rather, functions hru use hunxa

# dictionary maa value entry garne method:
d = {}
d['a'] = 'Apple'
d['b'] = 'Ball'
d['c'] = 'Cat'
d['d'] = 'Dog'
print(d)


# user accordingly dict bananune:
d = {}
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name. ")
    phone = int(input("Enter phone. "))
    d[name] = phone
print(d)

# key matra print hunxa:
d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
for i in d:
    print(i)

d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
for i in d.keys(): #keys() = keys print hune
    print(i)

d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
for i in d.items():  #items = sab print hune
    print(i)

d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
for i in d.values():   #values() = values print hune
    print(i)


#update garna:
d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
d['Satyam'] = 9808353479
print(d)

#del:
d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
del d['Satyam']
print(d)

#pop:
d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
d.pop('Satyam')
print(d)

d = {'Satyam': 9800000000, 'Shyam ': 9800000000}
b = {'Ram': 9803894765, 'Hari': 9876549083}
d.update(b)
print(d)

# list inside dict
d = {'Satyam': [9800000000,98000000], 'Shyam ': [9800000000,98000000]}
print(d)
print(d['Satyam'])
print(d['Satyam'][0])

# list inside dict where values are entered according to user's choice:
d = {}
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name. ")
    ntc_phone = int(input("Enter ntc number. "))
    ncell_phone = int(input("Enter ncell number. "))
    d[name] = [ntc_phone,ncell_phone]
print(d)

# dict inside list where value are entered according to user's choices:
l = []
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name. ")
    age = int(input("Enter age. "))
    add = input("Enter address. ")
    info = {'name':name,'age':age,'add':add}
    l.append(info)
print(l)

# dict inside dict:
a = {1:{'name':'Ram','age':34,'add':'Kathmandu'},
     2:{'name':'Shyam','age':23,'add':'Bhaktapur'},
     3:{'name':'Hari','age':30,'add':'Lalitpur'}}
print(a)

# dict inside dict in which the value is input according to the user's choice
d = {}
for i in range(1,3):
    name = input("Enter name. ")
    age = int(input("Enter age. "))
    add = input("Enter address. ")
    d[i] = {'name':name,'age':age,'add':add}
print(d)
print(d[1]['name'])