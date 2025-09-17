class Circle:
    def __init__(self,r):
        self.r=r
        print("Circle created!")
    def get_area(self):
        self.area = 3.14*3.14*self.r
        return f"Radius={self.r}\nArea={self.area}\n"
    
    def get_perimeter(self):
        self.perimeter = 2*3.14*self.r
        return f"Radius={self.r}\nPerimeter={self.perimeter}"

my_circle = Circle(10)
print(my_circle.get_area())       
print(my_circle.get_perimeter())
