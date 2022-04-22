"""
3. Write a Python class named Circle constructed by a radius and two methods which will
compute the area and the perimeter of a circle
"""


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return self.radius * 2 * 3.14


my_new_circle = Circle(10)
print(my_new_circle.area())
print(my_new_circle.perimeter())
