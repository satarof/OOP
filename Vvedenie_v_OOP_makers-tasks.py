'---------------------1-----------------------'

class Song:
    def __init__(self, title, author, year:int):
        self.title = title
        self.author = author
        self.year = year

    def show_title(self):
        return f'Название этой песни {self.title}'
    def show_author(self):
        return f'Автор этой песни {self.author}'
    def show_year(self):
        return f'Эта песня вышла в {self.year} году'

song = Song('Shape Of You', 'Ed Sheeran', 2016)

print(song.show_title())
print(song.show_author())
print(song.show_year())

'---------------------2-----------------------'

class Circle: 
    color='Синий' 
    pi = 3.14 
    def __init__(self,radius:int): 
        self.radius = radius 
    def get_area(self): 
        return self.pi * (self.radius**2) 
circle = Circle(2) 
circle.color = 'Черный' 
print(circle.color) 
print(circle.get_area())

'---------------------3-----------------------'

class BankAccount:
    balance = 0
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        print(f'Ваш баланс: {self.balance} сом')

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f'Ваш баланс: {self.balance} сом')

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
