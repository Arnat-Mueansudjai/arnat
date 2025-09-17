"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def get_area(self):
        area = self.__length*self.__width
        return f"Length={self.__length}\nWidth={self.__width}\nArea={area}\n"
    
    def get_perimeter(self):
        perimeter = (self.__length*2)+(self.__width*2)
        print(f"Length={self.__length}\nWidth={self.__width}\nPerimeter={perimeter}")
    
    def Is_square(self):
        if self.__length == self.__width:
            return True
        else :
            return False

myRetangle = Rectangle(10,5)
print(myRetangle.get_area())
myRetangle.get_perimeter()
print(myRetangle.Is_square())