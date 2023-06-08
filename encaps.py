# инкапсуляция - 1. сокрытие данных, 2. сбор атрибутов в одну капсулу

class A: 
    public = 'публичный'
    _protected = ''
    __private = 'asdfas'

@property
def func(self):
    return self.__private

@func.setter
def func(self, new_name):
    self.__private = new_name




# class B(A):
#     pass

# b = B()
# print(dir(b))

a = A()
a.func = 'private'
print(a.func)