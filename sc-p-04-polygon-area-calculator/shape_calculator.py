class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        self.area = self.height * self.width
        return self.area

    def get_perimeter(self):
        self.perimeter = ((2* self.width) + (2* self.height))
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (((self.height**2)+(self.width**2))**(1/2))
        return self.diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            picture = 'Too big for picture.'
        elif self.width < 50 and self.height < 50:
            picture = ((('*'* self.width) + '\n')* self.height)
        return picture
    
    def get_amount_inside(self, othero):
        self.amount_inside = ((self.height // othero.height) * (self.width // othero.width))
        return self.amount_inside
    
    def __str__(self):
        rectangle_str = ('Rectangle(width={}, height={})').format(self.width, self.height)
        return rectangle_str

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side

    def set_height(self, side):
        self.height = side
    
    def __str__(self):
        square_str = ('Square(side={})').format(self.width)
        return square_str