# rectangles in a qudrant where top left is the origin
# x axis is positive and increases as you move from left to right
# y axis is positive and increases as tou move from top to bottom

class Rectangle:
    def __init__(self, x, y, width, height):
        # initializes the instance attributes of a Rectangle object
        # x is the float x coordinate of the top left corner
        # y if the float y coordinate of the top left corner
        # width is the width of the rectangle as a float
        # height is the height of the rectangle as a float
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def display(self):
        # displays the rectangle by returning a string
        display_str = "x = " + str(self.x) + " y = " + str(self.y) + \
            " width = " + str(self.width) + " height = " + str(self.height)
        return display_str

    def top(self):
        # top is the y value of the top corners
        return self.y

    def left(self):
        # left is the x value of the left corners
        return self.x

    def right(self):
        # right is the x value of the right corners
        return self.x + self.width

    def bottom(self):
        # bottom is the y value of the bottom corners
        return self.y + self.height

    def collide_point(self, point):
        # point is a tuple (x,y)
        # returns bool
        # True if point inside border of rectangle, False otherwise
        within_x = point[0] >= self.left() and point[0] <= self.right()
        within_y = point[1] <= self.bottom() and point[1] >= self.top()

        return within_x and within_y

    def collide_rectangle(self, other):
        self_on_left = self.right() < other.left()
        self_on_right = self.left() > other.right()
        self_on_top = self.bottom() < other.top()
        self_on_bottom = self.top() > other.bottom()

        return not (self_on_left or self_on_right or self_on_top or self_on_bottom)


def main():
    red = Rectangle(25, 50, 50, 25)
    print(red.display())

    green = Rectangle(100, 100, 25, 50)
    print(green.display())

    pointA = (50, 63)
    pointB = (113, 125)

    print(red.collide_point(pointA))
    print(green.collide_point(pointB))

    blue = Rectangle(50, 63, 50, 25)
    print(red.collide_rectangle(blue))
    print(green.collide_rectangle(blue))


main()
