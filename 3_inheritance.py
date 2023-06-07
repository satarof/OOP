'============================Наследование======================'
# наследование - принцип ооп, в котором мы можем унаследовать методы и аттрибуты класса, так же переопределять и использовать 
# # 
# class A:
#     def method(self):
#         print('Метод в классе А')

# class B(A):
#     pass

# class C(A):
#     def method(self):
#         print('Метод в классе C')

# obj_B = B()
# obj_B.method()

# obj_C = C()
# obj_C.method()
'==================Types of inheritance================='
# odinochnoee
# mnojestvennoe
# mnogourovnevaya
# ierarhichwskaya
# hybrid

'-----------------Одиночное--------------------------'

# class A:
#     pass

# class B(A):
#     pass

'----------------множественное----------------------'

# class A:
#     def info(self):
#         print('A')

# class B:
#     def info(self):
#         print('B')

# class C(A, B):
#     pass

# obj_C = C()
# obj_C.info()
# print(C.mro())

'problems of mnojestvennogo nasledovaniya' 

" 1. Problem romba (reshena problema pri pomoshi mro)"
# class A:
#     def __str__(self) -> str:
#         return 'A'

# class B:
#     def __str__(self) -> str:
#         return 'B'

# class C:
#     def __str__(self) -> str:
#         return 'C'
    
# obj_c = C()
# print(obj_c)

' 2. Проблема перекрестного наследования (не решена)'
 
# class A:
#     pass

# class B:
#     pass

# class D(A,B):
#     pass

# class E(B,A):
#     pass

# class F(D,E):
#     pass

'---------------------------------Многоуровневая-------------------------'
# class A:
#     # info = 1
#     pass

# class B(A):
#     # info = 3
#     pass

# class C(B):
#     pass

# class E:
#     info = 2

#     def __str__(self):
#         return 'asd'

# class D(C,E):
#     pass

# obj_1 = D()
# print(obj_1.info)

'-----------------Иерархический----------------------------'

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(A):
#     pass

'----------------Гибридный-------------------------'

# class A:
#     pass

# class B:
#     pass

# class C(A,B):
#     pass

# class D(C):
#     pass

# class E(C):
#     pass

# class F(E):
#     pass

# class J(F):
#     pass

'------------------------------------------------------------'

# class A:
#     pass

# class B(A):
#     pass

# print(issubclass(A,B))

'------------------------------------------------------------'

"""
Создайте класс MyString, который будет наследоваться от str.

Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop."""

# class MyString(str):
    
#     def append(self, new_str):
#         return self + new_str
    
#     def pop(self):
#         popped = self[-1]
#         return self[:-1], popped


    # def __init__(self, string):
    #     self.string = string

    # def append(self, string1):
    #     self.string = self.string + string1
    #     return self.string
    
    # def pop(self):
    #     removed = self.string[-1]
    #     self.string = self.string[:-1]
    #     return removed
    
    # def __str__(self):
    #     return self.string
    
# obj = MyString('stroka')
# # print(obj)
# obj1 = obj.append('hello')
# print(obj1)
# print(obj.pop())



class A:
    def info(self, name):
        print(name)

class B:
    def info(self):
        super().info()
        print('B')

obj = B()
obj.info()