'=====================================Принципы ООП====================================='
# 1. Наследование 
# 2. Инкапсуляция 
# 3. Полиморфизм
# 4. Абстракция
# 5. Ассоциация --> Композиция и Агрегация 

# Наследование - позволяет принимать родителские методы, атрибуту и поведение

# Родительский класс
# Дочерний класс

'------------------------------------------------------------------------------------'
# class Animal: # родительский класс
#     def say(self):
#         print('I\'m an Animal')

# class Dog(Animal): # дочерний класс
#     def walk(self):
#         print('I\'m walking')

# class Croco(Animal): # дочерний класс
#     def say(self):
#         print('I\'m a croco')

# dog = Dog()
# dog.say()
# dog.walk()

# croco = Croco()
# croco.say()
# # croco.walk() # Error
'-------------------------------------------------------------------------------------'

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'Меня зовут {self.name}, мне {self.age} лет')

# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer
        
#     def info(self):
#         Person.info(self)
#         print(f'Я учусь в университете {self.univer}')
#     # def info(self):
#     #     super().info()
#     #     print(f'Я учусь в университете {self.univer}')

# bob = Student('Bob', 18, 'AUCA')
# bob.info()
# print(bob.name)

'-------------------------------------------------------------------------------------'

# class A:
#     def info(self):
#         print(1)

# class B:
#     def info(self):
#         print(2)

# class C(B,A):
#     def info(self):
#         super().info()
#         print(3)

# obj = C()
# obj.info()

'--------------------------------------------------------------------------------------------'

# class Employee:
#     bonus = 1.5
#     def __init__(self,name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'
    
#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_language):
#         super().__init__(name, last_name, salary)
#         self.lang = prog_language

# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps = None):
#         super().__init__(name, last_name, salary)
#         if emps == None:
#             self.emps = []
#         else:
#             self.emps = emps

#     def add_emp(self, emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#         else:
#             print('Employee already is in')

#     def show_emp(self):
#         result = []
#         for emp in self.emps:
#             result.append(emp.get_full_name())
#         return result        
    
# dev1 = Developer('Bob', 'Snow', 1500, 'Python')
# dev2 = Developer('Max', 'Korzh', 2000, 'Python + JS')
# dev3 = Developer('Lary', 'Kane', 1700, 'JS')
# dev4 = Developer('Steve', 'Rogers', 2500, 'Java')
# manager1 = Manager('Jasmina', 'Kurator', 1990, emps=[dev1,dev3])
# manager2 = Manager('Ertay', 'Xyz', 1990)

# manager2.add_emp(dev2)
# manager2.add_emp(dev2)
# manager2.add_emp(dev4)

# print(manager1.show_emp())
# print(manager2.show_emp())

# print(f'Manager {manager1.get_full_name()}, has {" ".join(manager1.show_emp())} developers. His salary is {manager1.salary}')

# manager1.give_bonus()

# print(f'Manager {manager1.get_full_name()}, has {" ".join(manager1.show_emp())} developers. His salary is {manager1.salary}')


'------------------------------------------------------------------------------------------------------------------------'
#CRUD
class Post:
    def __init__(self, user):
        self.user = user
        self.posts = []
        self.id = 0
    
    def create_post(self, title, body, image):
        self.id += 1
        post = dict(id=self.id, title=title, body=body, image=image)
        self.posts.append(post)
        return {'status':201, 'msg':'successfully created!'}

    def retrieve_post(self, post_id):
        for post in self.posts:
            if post.get('id') == post_id:
                return post
        return {'status':404, 'msg':'Not found!'}


    def update_post(self, post_id, **kwargs):
        for post in self.posts:
            if post.get('id') == post_id:
                post.update(**kwargs)
                return {'status':200, 'msg':'Udated'}
            return {'status':404, 'msg':'Not found!'}       

    def delete_post(self, post_id):
        for post in self.posts:
            if post.get('id') == post_id:
                self.posts.remove(post) # 1.
                # index_post = self.posts.index(post) # 2.
                # self.posts.pop(index_post)
                return {'status':200, 'msg':'Deleted'}
            return {'status':404, 'msg':'Not found!'}       
            

account1 = Post('Bob')
account2 = Post('Robert')

account1.create_post('Good News', 'Graduation', 'https://hips.hearstapps.com/hmg-prod/images/graduation-captions-lead-image-6412222f98500.jpg?crop=0.670xw:1.00xh;0.00801xw,0&resize=1200:*')
account1.create_post('Bad News', 'GRT = 99', 'https://www.ohlone.edu/sites/default/files/styles/hero_slideshow/public/groups/Student_Services/photos/headshots/class_of_2023_graphic.png?itok=6fOJWGdV')

# print(account1.posts)
# print(account1.retrieve_post(2))
# print(account1.update_post(1,title='okay news', body='nice', image='https://www.freedomforum.org/content/uploads/2022/05/FirstFive_5.18.22.jpg'))
# print(account1.retrieve_post(1))
print(account1.delete_post(1))
print(account1.retrieve_post(1))
