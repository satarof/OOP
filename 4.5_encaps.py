# инкапсуляция - 1. сокрытие данных, 2. сбор атрибутов в одну капсулу

# class A: 
#     public = 'публичный'
#     _protected = ''
#     __private = 'asdfas'

# @property
# def func(self):
#     return self.__private

# @func.setter
# def func(self, new_name):
#     self.__private = new_name




# class B(A):
#     pass

# b = B()
# print(dir(b))

# a = A()
# a.func = 'private'
# print(a.func)

# class A:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
    
#     @name.deleter
#     def name(self):
#         del self.__name

# a = A('Tima')
# print(a.name)
# del a.name


list_ = list(range(1,11))
del list_[5]
print(list_)