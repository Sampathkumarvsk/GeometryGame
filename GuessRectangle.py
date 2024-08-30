from random import randint

from Point import Point
from Rectangle import Rectangle

rectangle = Rectangle(Point(randint(0,9),randint(0,9)), Point(randint(10,19),randint(10,19)))
print("Rectangle Co-ordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",rectangle.upright.y)

user_point = Point(float(input("Guess X:"  )), float(input("Guess Y:"  )))
user_area = (float(input("Guess rectangle area ")))
print("Your point is inside the rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area is off by : ", rectangle.area()- user_area)
