#!/usr/bin/python3
"""Contains the ``Rectangle`` class definition.
"""
from models.base import Base


class Rectangle(Base):
    """``Rectangle`` class definition.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance of class ``Rectangle``.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns the string representation of the `Rectangle` object.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """``width`` property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """``height`` property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """``x`` property.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) == int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """``y`` property.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) == int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Returns the area of the Rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints out the rectangle to the screen.
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """Updates each attribute of the class
        """
        if args is not None and len(args) != 0:
            if len(args) == 1:
                super().__init__(args[0])
            elif len(args) == 2:
                id, width = args
                super().__init__(id)
                self.width = width
            elif len(args) == 3:
                id, width, height = args
                super().__init__(id)
                self.width = width
                self.height = height
            elif len(args) == 4:
                id, width, height, x = args
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
            elif len(args) == 5:
                id, width, height, x, y = args
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y
        else:
            if kwargs is not None:
                for key in kwargs.keys():
                    if key == 'id':
                        super().__init__(kwargs[key])
                    elif key == 'width':
                        self.width = kwargs[key]
                    elif key == 'height':
                        self.height = kwargs[key]
                    elif key == 'x':
                        self.x = kwargs[key]
                    elif key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        """returns the dictionary representation of the ``Rectangle``
        instance
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
