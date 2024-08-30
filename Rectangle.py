from Point import Point
class Rectangle:
    def __init__(self,lowleft,upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

pointx = Point(6,7)


rectanglex = Rectangle(Point(5,6), Point(7,9))

pointx.falls_in_rectangle(rectanglex)
