'===========================================Инкапсуляциия==============================================='
#инкапсуляция - это принцип ООП, у которого есть 2 трактовки
#1. сбор всех необходимых аттрибутов в одну "капсулу" (класс)
#2. сокрытие данных (огрраничение доступа к аттрибутам)

'виды доступа к аттрибутам'
#1. public (публичный)
#2._protected (защищённый) - с одним underscore в начале
#3.__private (приватный) - с двуми underscore в начале

# class A:
#     attrs1 = 'public'
#     _attrs2 = 'protected'
#     __attrs3 = 'private'

# print(A.attrs1)
# print(A._attrs2)
# print(A.__attrs3) # error AttributeError
# print(A._A__attrs3)

'----------------------------------------------------------------'

# class B:
#     x = 'hello'

#     def __init__(self):
#         self.y = 'world'
#         self.__private = 'hw' 

# obj_b = B()  
# print(obj_b.__dict__)

# obj_b.hello = 'HELLO'
# print(obj_b.__dict__)

# setattr(obj_b, 'new', 'Hew Var')
# print(obj_b.__dict__)


'===============================Getters/Setters====================================='
# функции с помощью которых можно получить/изменить значение атрибутов 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         if new_age > 0 and new_age < 120:
#             self.__age = new_age

#         else:
#             raise Exception('Возраст не может быть меньше 0 или больше 120')
        
# obj = Person('Ertay', 25)
# print(obj.get_age())
# # print(obj._Person__age)

# obj.set_age(50)
# print(obj.get_age())

'-----------------------------------------------'

# c'[lass Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.__age = age

#     'декоратор property делает из функции --> атрибут'
#     @property
#     def age(self):
#         return self.__age
    
#     'переопределяет __getattribute__ в объекте age (property))'
#     @age.getter
#     def age(self):
#         return self.__age
    
#     'декоратор setter вызывается когда пишется obj.age = "value"'
#     @age.setter
#     def age(self, new_age):
#         if type(new_age) != int:
#             raise Exception('Введите возраст цифрами')
#         if new_age > 0 and new_age < 120:
#             self.__age = new_age

#         else:
#             raise Exception('Возраст не может быть меньше 0 или больше 120')
        
#     'декоратор deleter вызывается когда пишется del obj.age'   
#     @age.deleter
#     def age(self):
#         if self.__age < 100:
#             raise Exception('невозможно удалить возраст')
#         del self.__age

# obj = Person('Kurmanzhan', 23)
# print(obj.age)
# obj.age = 112
# del obj.age
# print(obj.__dict__)

'------------------------------------------------------------'

class Phone:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        assert type(new_number) == str, 'Номер должен быть строкой '
        assert len(new_number) == 9, 'Номер должен состоять из 9 цифр'

        n = new_number
        '+996 123-45-67-89'
        self.__number = f'+996 {n[:3]}-{n[3:5]}-{n[5:7]}-{n[7:]}'

obj = Phone('+996 123-45-67-89')
print(obj.number)

obj.number = '773120192'
print(obj.number)

# obj._Phone__number = '666218932'
# print(obj._Phone__number)

