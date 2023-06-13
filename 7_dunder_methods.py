'=====================================Dunder Methods(Магические методы)(Дандер методы)================================'
# Магические методы (dunder - double underscore) - методы, у которых 2 нижних пробела в начале и в конце, магия в том что мы их вызываем ненапрямую, а они вызываются определенными операторами или функциями

# __new__, __init__ - int('10')

# __str__ 
a = 5 

a = 6
b = 7

# __eq__
a == b
a.__eq__(b)

# __ne__
a != b
a.__ne__(b)

# __lt__
a < b
a.__lt__(b)

#__gt__
b > a
b.__gt__(a)

# __le__
a <= b
a.__le__(b)

# __ge__
b >= a
b.__ge__(a)

# a = 10 
# b = a.__rxor__()
# print(b)

# b = 10 
# a = b.__float__()
# print(a)

# string = 'hello'
# string.lower
# print(string.__getattribute__('upper'))
# print(getattr(string, 'lower', 'Not found'))

# string = ' hello'
# print(string[0])
# print(string.__getitem__(0))

# dict_ = {'a':1, 'b':2}
# print(dict_.__getitem__('a'))

'-----------------------------------------------------------------'
# Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len).

# Создайте обьекты word1 и word2 класса Word и сделайте сравнения.
class Word:
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return len(self.word) == len(other)

    def __gt__(self, other):
        return len(self.word).__gt__(len(other))
        

    def __lt__(self, other):
        return len(self.word).__lt__(len(other))



    def __ge__(self,other):
        return len(self.word).__ge__(len(other))


    def __le__(self,other):
        return len(self.word).__le__(len(other))
    
obj1 = '1234568'
obj2 = '1234567'
print(obj1 == obj2)


# class Word:
#     def __init__(self, word):
#         self.word = word

#     def __gt__(self, other):
#         return len(self.word) > len(other.word)

#     def __lt__(self, other):
#         return len(self.word) < len(other.word)

#     def __ge__(self, other):
#         return len(self.word) >= len(other.word)

#     def __le__(self, other):
#         return len(self.word) <= len(other.word)

