from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Square(Shape):
    def area(self): return 16

s = Square()
print(s.area())
