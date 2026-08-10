from abc import ABC, abstractmethod
import math

#인터페이스 역할을 하는 추상 클래스 
class Shape(ABC): #class abstract Shape(){}
    
    @abstractmethod
    def area(self): #public void area(){};
        pass # 추상 메서드 
    
    @abstractmethod 
    def perimeter(self):
        pass 
    
class Circle (Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    #OverWriting     
    def area(self):
        return math.pi * self.radius**2
    #오버 라이딩 
    def perimeter(self):
        return 2*math.pi*self.radius
    
class Rectangle (Shape) :
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class EqualTriangle (Shape) :
    
    def __init__(self, side, height):
        self.side = side
        self.height = height
    
    def area(self):
        return (self.side * self.height) /2
    
    def perimeter(self):
        return 3 * self.side 
    
#main

circle1 = Circle(5)
rectangle1 = Rectangle(4,7)
equalTriangle1 = EqualTriangle(5,8)

print("원의 넓이: ", circle1.area())
print("원의 둘래: ", circle1.perimeter())
print("--------------------------------------")

print("직사각형의 넓이: ", rectangle1.area())
print("직사각형의 둘래: ", rectangle1.perimeter())
print("--------------------------------------")

print("정삼각형의 넓이: ", equalTriangle1.area())
print("정삼각형의 둘래: ", equalTriangle1.perimeter())
print("--------------------------------------")




    
   