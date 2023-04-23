class Rectangle:

  # Initializes the object with two parameters (width, height):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # set methods:
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  # Returns a string (or f-string):
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  # Returns area:
  def get_area(self):
    return self.width * self.height

  # Returns perimeter:
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  # Returns diagonal:
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    # If the width or height is larger than 50, returns:
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
      # else returns a string that represents the shape:
    else:
      # - one row is a line of '*' with the same lenght as the shape width
      row = '*' * self.width 
      # - the number of rows is the same as the shape height 
      rows = [row for _ in range(self.height)] 
      # - the shape picture is just a grid of '*'
      grid = '\n'.join(rows)
      return grid + "\n"

  # Returns the number of times the passed in shape could fit inside the shape:
  def get_amount_inside(self, second_shape):
    # floor division
    return self.get_area() // second_shape.get_area()


# child object:
class Square(Rectangle):

  # Initializes the object with one parameter (side):
  def __init__(self, side):
      self.width = side
      self.height = side

  def __str__(self):
    return f'Square(side={self.width})'

  # set method:
  def set_side(self, side):
    self.width = side
    self.height = side

