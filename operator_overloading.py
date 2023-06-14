class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1+p2)

#
class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} {self.y}"
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1+p2)

# 
class Point:
    def __init__(self,x = 0):
        self.x = x
        print("This is init method",self.x)
    
    def __str__(self):                                          #str method le object return garchha
        print(f"This is str method {self.x}")
        return f"{self.x}"
    
    def __add__(self,other):
        x = self.x + other.x
        print("This is add method",x)
        return Point(x)
    
p1 = Point(2000)
p2 = Point(3000)
p3 = Point(1500)
print(p1+p2+p3)

# Polymorphism
class Parrot:
    def fly(self):
        print("Parrot can fly.")
    def swim(self):
        print("Parrot can't swim.")
class Penguin:
    def fly(self):
        print("Penguin can't fly.")
    def swim(self):
        print("Penguin can swim.")
# common interface
def flying_test(bird):
    bird.fly()
def swimming_test(bird):
    bird.swim()
# instantiate objects 
blu = Parrot()
peggy = Penguin()
# passing the object
flying_test(blu)
flying_test(peggy)
swimming_test(blu)
swimming_test(peggy)