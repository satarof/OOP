'''
Полиморфизм - принцип ООП, в котором в разных классах методы называются одинково, но имеют другой функционал (другая реализация) 
'''

# class Dog:
#     def speak(self):
#         print('ГАв-гАФ')

# class Cat:
#     def speak(self):
#         print('МяУ-Мяу')
        
# class Cow:
#     def speak(self):
#         print('МУУ-Муу')

# objects = [Dog(), Cow(), Cat(), Cow(), Cat(), Dog()]

# # for obj in objects:
# #     obj.speak()
        
# #___add__
# print(5+5) # int 10 - складываются 
# print('5'+'5') # str 55 - конкатенация
# print([1,2,3]+[4,5,6]) # list [1,2,3,4,5,6]   - конкатенация

# a = 5
# b = 6
# print(a.__add__(b))


class A:
    def __str__(self) -> str:
        return 'i\'m str'
    
    def __repr__(self) -> str:
        return 'i\'m repr'
    
a = A()
print(a)
print(repr(a))

#ToDO - узнать различие __str__ от __repr__

class A:
    age = 7

    def __init__(self, name) -> None:
        self.name = name

a = A('ertay')
a.last_name = 'esenbekov'
print(a.__dict__)
