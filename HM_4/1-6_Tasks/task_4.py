"""
4. Write a Python class named Rectangle constructed by a length and width and a
method which will compute the area of a rectangle
"""


class Rectangle():
    def __init__(self, l, w):
        self.lenght = l
        self.witdh = w

    def area(self):
        return self.lenght * self.witdh


my_new_rectangle = Rectangle(8, 10)
print(my_new_rectangle.area())
