"""Q. Description: You are tasked with creating a Rectangle class with the following requirements:
1.	An instance of the Rectangle class requires length:int and width:int to be initialized.
2.	We can iterate over an instance of the Rectangle class 
3.	When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
"""

class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def __iter__(self):
    yield{"length": self.length}
    yield{"width": self.width}

recObj = Rectangle(27, 16)

for attr in recObj:
  print(attr)


"""To check the output just run 😃"""