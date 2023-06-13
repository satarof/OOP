'================Methods================='
# There are 3 methods

# instance methods - regular methods that accept the first argument self(link to the object), nujny for the work with attributes of object.
# instance methods - обычные методы, которые принимают первым аргументом self(ссылку на обьект), нужны для работы с аттрибутами объекта

# class A:
#     def instance_methods(self):
#         print('the first argument', self)

# obj_a = A()
# obj_a.instance_methods()

# class methods - methods that accept the first argument cls(link to the class), nujny for creation of objects or for the change of attributes of the class, for the creation of class method - nujno zadecoritovat' ego classmethod
# class methods - методы, которые принимают первым аргументом cls(ссылка на класс), нужны для создания обьектов или изменения аттрибутов класса, для создания метода класса нужно задекорировать его classmethod

'--------------------------------------------------------------------------'

# class B:
#     @classmethod
#     def class_method(cls):
#         print('the first argument', cls)

# obj_b = B()
# obj_b.class_method()


# class C:
#     counter = 0

#     def  __init__(self):
#         self._inc_counter()

#     def __del__(self):
#         self._dec_counter()
#         del self

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

#     @classmethod
#     def _dec_counter(cls):
#         cls.counter -= 1

# obj_1 = C()
# obj_2 = C()
# obj_3 = C()
# del obj_2
# print(C.counter)

'------------------------------------------------------------'

# class Pizza:
#     def __init__(self, radius, *ingredients):
#         self.r = radius
#         self.ingredirents = ingredients

#     def cook(self):
#         print(f'Готовится размера {self.r*2} см ')
#         print(f'Ингридиенты {self.ingredirents}')
    
#     @classmethod
#     def four_cheeze(cls, r):
#         pizza = cls(r, 'Моцарелла', 'Брынза', 'Чеддер', 'Ламбер')
#         return pizza
    
# pizza1 = Pizza(15, "пеперони", "помидоры", "соус")
# pizza2 = Pizza.four_cheeze(12)
# pizza3 = Pizza.four_cheeze(20)

# pizzas = [pizza1, pizza2, pizza3]
# for pizza in pizzas:
#     pizza.cook()

'-------------------------------------------------------------'

#static methods - простая функция, который не взаимодействует ни с объектом, ни с классом, поэтому не влияет на состояние класса, объекта

# class D:
#     @staticmethod
#     def hello(string):
#         print(string)

# obj_d = D()
# obj_d.hello('hello world')

'------------------------------------------------------------'

class Cylinder:
    def __init__(self, diameter, hight):
        self.di = diameter
        self.h = hight
        self.area = self.get_area(diameter, hight)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle = pi*di**2/4
        side = pi*di*h
        area = circle * 2 * side
        return area
    
cylinder = Cylinder(4,10)
print(cylinder.area)

area2 = Cylinder.get_area(2,5)
print(area2)
