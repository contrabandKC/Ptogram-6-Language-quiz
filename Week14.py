##########################################################################
# CS 101
# Program : Lab 14 Inheritance
# Name Erik Marquez
# Email eemxr9@mail.umkc.edu
# PROBLEM : Inheritance
###########################################################################
import turtle


class Point(object):
    '''Master Class, sets origin, and puts the pen down to draw'''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    """uses point as the master class, uses point to draw a box,
    with x1, y1, width, height, color"""

    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1,y1,color)
        self.width = width
        self.height = height

    def draw_action(self):
        """Draw Box"""

        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class BoxFilled(Box):
    """Inherits from the box class but adds the ability to add fill color"""

    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        """Draw filed box"""
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    """uses point as the master class, uses point to draw a circle,
    with x1, y1, width, height, color"""

    def __init__(self,x1,y1,radius,color):
        super().__init__(x1,y1,color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)


class CircleFilled(Circle):
    """Inherits from the circle class but adds the ability to add fill color"""

    def __init__(self,x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        """Draw filed circle"""
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


p = Point(-100,100,"blue")
p.draw()

b = Box(100,110,50,40,"red")

b.draw()

bf = BoxFilled(200,-200,100,200,"red", "Blue")

bf.draw()

c = Circle(-30,30, 100, "orange")
c.draw()


cf = CircleFilled(-200, 200, 100, "orange", 'black')

cf.draw()


print('\nThank you for playing!')
