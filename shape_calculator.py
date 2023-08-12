# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-polygon-area-calculator#shape_calculator.py

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ""
        if self.height > 50 or self.width > 50:
            too_big_error = "Too big for picture."
            return too_big_error
        else:
            for i in range(self.height):
                picture += "*" * self.width + "\n"
            return picture

    def get_amount_inside(self, new_shape):
        area_1 = new_shape.get_area()
        result = self.get_area() / area_1
        return int(result)

    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        Rectangle.set_height(self, self.side)
        Rectangle.set_width(self, self.side)

    def set_side(self, new_side):
        self.side = new_side
        Rectangle.set_height(self, self.side)
        Rectangle.set_width(self, self.side)

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)

    def __repr__(self):
        return "Square(side=" + str(self.side) + ")"
