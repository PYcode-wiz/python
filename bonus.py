# comprehension: list, dictionary
l = [int(input("Enter any value: ")) for i in range(5)]
print(l)

l = sum([int(input("Enter any value: ")) for i in range(5)])
print(l)

d = {i:i**2 for i in range(5)}
print(d)

d = {input("Enter your name: "):int(input("Enter your phone: ")) for i in range(1,3)}
print(d)

# date and time:
import datetime
t = datetime.datetime.now()
print(t)

date = datetime.datetime.now()
print(date.strftime("%D"))


date = datetime.datetime.now()
print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)


import datetime
a = datetime.datetime.now()
n = input("Enter name: ")
b = datetime.datetime.now()
print(b-a)

# os package:
import os 
print(os.listdir())

# creating folder using os:
import os
os.mkdir("python")

# entering a folder using os:
os.chdir("python")
# then type pwd in the terminal.

# renamining a folder using os:
os.rename("python","new_folder")

# removing FILE using os:
os.remove("data.csv")

# removing FOLDER using os:
os.rmdir("python")