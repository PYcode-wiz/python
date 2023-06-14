# file handling

# file = open('<file_name','<mode>')
# <operation>
# file.close()

# with open('<file_name>','<mode>') as file:
#     <operations>
# different types of modes 
# read -> r
# create -> x
# write -> w 
# append -> a 

file = open('data.txt','x')
file.close()

file = open('data.txt','r')
y = file.read()
print(y)
print(type(y))
file.close()

lines = y.split("\n")
print(lines)

file = open('data.txt','w')
file.write('Hello World')
file.close()

grand_total = 0
s = ""
file = open ('bill.csv','w')
file.write('name,price,quantity.total\n')
n = int(input("Enter n = "))
for i in range(n):
    product_name = input("Enter product name = ")
    price = int(input("Enter price = "))
    qty = int(input("Enter quantity = "))
    info = f"{product_name},{price},{qty}\n"
    total = price * qty
    grand_total = grand_total + total
    s = s + info 
print("All total = ",grand_total)
file.write(s)
file.close()