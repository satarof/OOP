'=================================Абстракция======================='
# Абстракция - принцип ООП, в которм создается класс пустышка, где задаются названия методов и аттрибутов, для того, чтобы в дочерних классах не забыть их переопределить

# from abc import ABC, abstractmethod, abstractproperty
# class AbstractAnimal(ABC):
#     @abstractproperty
#     def legs(self):
#         pass
    
#     @abstractmethod
#     def voice(self):
#         pass

# # class Dog(AbstractAnimal):
# #     pass


# # class Dog(AbstractAnimal):
# #     def voice(self):
# #         print('гав гав')

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('гав гав')

# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('мяу мяу')


# obj = Dog()
# obj.voice()
# print(obj.legs)

# obj_2 = Cat()
# obj_2.voice()
# print(obj_2.legs)

' Абстрактный метод у которого есть объявление, но нет реализации'

from abc import ABC, abstractmethod
from math import pi
from typing import Any

# class Shape(ABC):
#     def __init__(self,name):
#         self.name = name

#     # абстрактный метод который необходимо переопределять для каждого наследонного класса
#     @abstractmethod
#     def area(self): pass

#     # общий метод, который будут использовать все наследники этого класса
#     def fact(self):
#         print('Я фигура в двухмерной плоскости')

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__('Квадрат')
#         self.length = length
    
#     def area(self):
#         return self.length**2
    
#     def fact(self):
#         super().fact
#         print(f'я {self.name}, у меня все углы по 90 градусов')

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Круг')
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2
    
# a = Square(4)
# print(a.area())
# a.fact()

# b = Circle(3)
# print(b.area())
# b.fact()


class ChessPiece(ABC):
    def draw(self):
        print('drew a chess piece!')
    
    @abstractmethod
    def move(self): pass

class Queen(ChessPiece):
    def move(self):
        print('Могут двигаться по вертикали, по горизонтали, по диагонали на любую длину')

class Pawn(ChessPiece):
    def move(self):
        print('Могу двигатьмя на одну клетку, либо вначале на две')

q = Queen()
q.draw()
q.move()

p = Pawn()
p.draw()
p.move()
    