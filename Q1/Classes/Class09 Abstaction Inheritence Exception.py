class A:
    def __init__(this, name, age):
        this.__name = name
        this.__age = age

    def display(this):
        print(this.__name + "\n" + str(this.__age))

    def change(this, name, age):
        this.__name = name
        this.__age = age


ali = A("Ali", 123)
ali.display()
ali.change("Ali Muhammad", 21)
ali.display()


class Abstract1:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(Abstract1):
    pass


ob1 = Abstract1(2, 5)
print(ob1.a)
print(ob1.b)
ob2 = B(7, 9)
print(ob2.a)
print(ob2.b)

from abc import ABC, abstractmethod


class Abstract2(ABC):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def abstractMethod(self):
        pass


class Abstract3(Abstract1):
    def __init__(self, a, b):
        super(Abstract3, self).__init__(a, b)

    def abstractMethod(self):
        pass

    pass


obj = Abstract3(2, 5)
print(obj.a)
print(obj.b)


class Object:

    def __init__(self, name):
        self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Shape(Object, ABC):

    def __init__(self, name):
        super(Shape, self).__init__(name)
        pass

    @abstractmethod
    def getArea(self):
        pass


class Square(Shape):

    def __init__(self, name, length, width):
        super(Square, self).__init__(name)
        try:
            int(length)
            int(width)
        except:
            raise Exception
        self.__length = length
        self.__width = width

    def setWidth(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width

    def setLength(self, length):
        self.__length = length

    def getWidth(self):
        return self.__length

    def getArea(self):

        return self.__length * self.__width


try:
    obj = Square("Bedroom", 23, 34)
    print(obj.getArea())
except:
    print("Invalid Data Type, Enter length.width as int")