#!/usr/bin/python3
"""
rectangle module
"""
from base import Base


class rectangle(Base):
    """
    rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)


            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
if __name__ == "__main__":
    r1 = rectangle(10, 2)
    print(r1.id)

    r2 = rectangle(2, 10)
    print(r2.id)

    r3 = rectangle(10, 2, 0, 0, 12)
    print(r3.id)
