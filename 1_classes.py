'===============================OOP============================'
# # OOP - Object-orientated programing
# # ООП - Обьектно ориентированное программирование(парадигма)

# class Person:
#     # переменные внутри класса (объекта) - аттрибуты
#     arms = 2
#     legs = 2
#     head = 1

#     # функции внутри класса - методы
#     def __init__(self, age, name):
#         # init - метод, который будет добавлять в обьект те аттрибуты, которые отличаются у разных обьектов
#         # self - ссылка на обьект, который только что создался
        
#         self.age = age
#         self.name = name

#     def walk(self):
#         print(f'{self.name} ходит')

#     def happy_birthday(self):
#         print(f'{self.name}, с днем рождения')
#         self.age += 1
#         return 'Подарок'
    
# obj1 = Person(20, 'Maks')
# obj2 = Person(23, 'Vova')

# print(obj1.arms)
# print(obj1.name, obj1.age)
# obj1.happy_birthday()
# print(obj1.age)

# print(obj2.arms)
# print(obj2.name, obj2.age)
# obj2.happy_birthday()
# print(obj2.age)

'=========================Объекты класса===================='
# объект, экземпляр, instance класса - сущность, созданная по шаблону класса (он перенимает все атрибуты и методы класса)

'=========================Атрибуты и методы======================'
# # атрибуты - переменные
# # методы - функции

# class A: 
#     var1 = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная объекта'

#     def __str__(self):
#         return 'Объекты от класса А'
    
# print(dir(A))
# # в списке нет переменной var2, так как мы распечатали все методы и атрибуты имеено класа
# obj = A()
# print(dir(obj))
# # в списке есть var2 и var1, так как мы распечатали все методы и атрибуты именно объекта

# print(A)

'----------------------------------------------------------------------------'

# class Calc:
#     def add(self, a,b):
#         return a + b
    
#     def sqrt(self, num):
#         import math
#         sqrt_num = math.sqrt(num)
#         return sqrt_num
    
#     def precent(self, total, _precent):
#         return(total * _precent) / 100
    
#     def super_func(self, string):
#         return eval(string)
    
# calc = Calc()
# print(calc.add(4,5)) #9
# print(calc.sqrt(4)) # 2.0
# print(calc.precent(67,10)) # 6,7
# print(calc.super_func('10-5*3/2')) # 2.5

# class B:
#     var = 4

#     def __init__(self, a ):
#         self.a = a

# obj = object.__new__(B)
# B.__init__(obj, 5)  
# obj.__init__(5)
# print(obj.a)

# class Sniper:
#     health = 100

#     def __init__(self, name):
#         self.name = name

#     def shoot(self, sniper):
#         sniper.health -=20
#         print(f'атаковал {self}')
#         print(f'У {sniper2} осталось {sniper2.health}')

#     def __str__(self):
#         return self.name

# sniper1 = Sniper('Tom')
# sniper2 = Sniper('Bob')

# import random
# while sniper1.health and sniper2.health:
#     choice = random.randint(1,2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f'Победил {sniper1.name}, {sniper1.health}')
# else:
#     print(f'Победил {sniper2.name}, {sniper2.health}')

'----------------------------------------------------------------------------'

# class Car:
#     def __init__(self, model):
#         self.model = model

#     def __str__(self):
#         return self.model
    

# obj1 = Car('BMW X8')
# print(obj1)

# obj2 = Car('Mercedes-Benz S class')
# print(obj2)

'------------------------------------------------------------------------------'

# class Soda: 
#     def __init__(self, ing=None):
#         if isinstance(ing, str):
#             self.ing = ing
#         else:
#             self.ing = None

#     def show_my_drink(self):
#         if self.ing:
#             print(f'Газировака из {self.ing}')
#         else:
#             print('Простая газировка')


# obj1 = Soda('Strawberry')
# obj1.show_my_drink()

# obj2 = Soda(1)
# obj2.show_my_drink()

# obj3 = Soda()
# obj3.show_my_drink()

# obj4 = Soda('Apple')
# obj4.show_my_drink()

'---------------------------------------------------------------------------------'

# class A:
#     pass

# class B:
#     pass

# class C:
#     def __init__(self,obj):
#         if isinstance(obj, A):
#             print(f'Объект относится к классу А')

#         elif isinstance(obj, B):
#             print(f'Объект относится к классу B')       

# obj1 = A()
# obj2 = B()

# objC = C(obj1)
        
'--------------------------------------------------------------------------------'

# #[5,6,7]
# # a + b > c

# class TriangleChecker:
#     def __init__(self, sides):
#         self.sides = sides

#     def is_triangle(self):
#         if any(type(side) == bool for side in self.sides):
#             return 'Нужно вводить только числа'
#         if not all(isinstance(side, (int, float)) for side in self.sides):
#             return 'Нужно вводить только числа'
#         if not all(side>0 for side in self.sides):
#             return 'Число должно быть выше нуля'
#         sorted_list = sorted(self.sides)
#         if sorted_list[0] + sorted_list[1] < sorted_list[2]:
#             return 'Такого треугольника не существует'
#         return 'Такой треугольник существует'

# obj1 = TriangleChecker([6,3,True])
# print(obj1.is_triangle())

# obj2 = TriangleChecker([77,1,2])
# print(obj2.is_triangle())

# obj3 = TriangleChecker([2,3,-10])
# print(obj3.is_triangle())

# obj4 = TriangleChecker([3,4,2])
# print(obj4.is_triangle())

# obj5 = TriangleChecker(['asd',21,'asd'])
# print(obj5.is_triangle())

'-----------------------------------------------------------------------'

# class Human:
#     def __init__(self):
#         print('init worked!')
#         self.raychel = 'raychel'
#         self.golod = 100

#     def eat(self, meal, doela=True):
#         print(f'{self.raychel} покушала {meal}')
#         if doela:
#             if self.golod < 50:
#                 self.golod = 0
#             else:
#                 self.golod -= 50
#         else:
#             self.golod -= 25

# obj = Human()
# print(obj.raychel, obj.golod)

# obj.eat('burger', doela=False)
# print(obj.golod)

# obj.eat('kruasan')
# print(obj.golod)

# obj.eat('kruasan')
# print(obj.golod)

# obj.eat('kruasan')
# print(obj.golod)



class phone_numbers_book:
  def __init__(self, name, surname, phonenumber):
    self.name = name
    self.surname = surname
    self.phonenumber = phonenumber

  def get_info(self):
    return f'Контакт: {self.name} {self.surname} , телефон: {self.phonenumber}'