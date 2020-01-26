"""
Spyder Editor

This is a temporary script file.
"""


class Student:
    # global variable (Class variable) Accessible through both class name and object Same throughout code
    counter = 0;

    def __init__(this, sid, sname, fname, course, fee, password):
        this.__sid = sid
        this.__sname = sname
        this.__fname = fname
        this.__course = course
        this.__fee = fee
        this.__password = password
        Student.counter += 1

    def getID(this):
        return this.__sid

    def setID(this, sid):
        this.__sid = sid

    def getName(this):
        return this.__sname

    def setName(this, sname):
        this.__sname = sname

    def getCourse(this):
        return this.__course

    def setCourse(this, course):
        this.__course = course

    def getFname(this):
        return this.__fname

    def setFname(this, fname):
        this.__fname = fname

    def getFee(this):
        return this.__fee

    def setFee(this, fee):
        this.__fee = fee

    def getPassword(this):
        return this.__password

    def setPassword(this, password):
        this.__password = password

    def login(this, username, password):
        return username.getPassword() == password

    def logout(this):
        pass


waleed = Student(123, "Waleed Butt", "Amer Butt", "AI", 1000, "0110")
waleed1 = Student(123, "Waleed Butt", "Amer Butt", "AI", 1000, "0110")
waleed2 = Student(123, "Waleed Butt", "Amer Butt", "AI", 1000, "0110")
waleed3 = Student(123, "Waleed Butt", "Amer Butt", "AI", 1000, "0110")
waleed4 = Student(123, "Waleed Butt", "Amer Butt", "AI", 1000, "0110")

try:
    print(waleed.sname)
except:
    print("Error Private Variable")
print(waleed.getID(), end=" ")
print(waleed.getName())
print(waleed.counter)
print(waleed1.counter)
print(waleed2.counter)
print(waleed3.counter)
print(Student.counter)

print(waleed.login(waleed1, "0110"))


# Inheritace
class Animal:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age=""):
        self.__age = age

    def getAge(self):
        return self.__age

    def sound(self):
        return "Hello"


class LivingBeings:
    def __init__(self):
        pass

    def lives(self):
        return "Home"


class Dog(Animal, LivingBeings):
    def __init__(self, name, age):
        LivingBeings.__init__(self)
        Animal.__init__(self, name, age)

    def sound(self):
        return "Woof"

    def lives(self):
        return "Dog House"


jack = Dog("Jack", 12)
print(jack.sound());
print(jack.lives());

# Polymorphism