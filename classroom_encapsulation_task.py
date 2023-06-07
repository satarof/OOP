"""
Классная работа
По теме: Инкапсуляция

Создайте класс Terminal. Создайте объект-карточку от этого
класса, передав номер своей карточки и пин код. При этом,
необходимо проверить валидность карточки: номер карточки
должен содержать строго 16 цифр, а пин код - 4 цифры (для этого
используйте инкапсуляцию). При создании карточки в ней
содержится 0 сом. Далее в классе должны быть следующие
методы:

 метод put, который будет принимать в качестве
аргументов: пин код карточки, вторым аргументом -
сумму денег, которую вы хотите закинуть на эту
карточку. Прежде, чем закидывать деньги, необходимо
проверить введенный пин код на совпадение
(используйте инкапсуляцию)
 метод get_money, который также принимает первым
аргументом пин код, вторым аргументом - сумму денег,
которую вы хотите извлечь из карточки. Здесь также
необходимо использовать валидацию: проверка пин
кода + сумма денег должна быть округленной до
десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67,
899, 45.6 - невалидные данные). И только после
проверки деньги извлекаются.

Примените данные методы к своей карточке несколько раз и в
конце выдайте, сколько денег на карточке. Примечание: нельзя
извлечь сумму денег, если она больше, чем сумма денег на
карточке; также нельзя вытащить пин код карточки (эти данные
должны быть скрыты)
"""


from functools import reduce

class Terminal:

    def __init__(self, card_number, code):
        self.card_number = card_number
        self.__code = code
        self.balance = 0

    def put(self, pin, amount):
        if pin == self.__code and isinstance(amount, int) and amount > 0:
            self.balance += amount
            print(f"Успешное зачисление {amount} сом в карту.")
        else:
            print("Неправильлный пароль или недопустимая сумма денег.")

    def get_money(self, pin, amount):
        if pin == self.__code and isinstance(amount, int) and amount > 0 and amount <= self.balance and amount % 10 == 0:
            self.balance -= amount
            print(f"Успешное снятие {amount} сом с карты. ")
        else:
            print("Неправильлный пароль или недостаточный баланс")

    def check_balance(self):
        print(f"текущий баланс: {self.balance} сом.")

    @property
    def code(self):
        return reduce(lambda x, y: x + y, ['*' for _ in range(4)])
    
    @code.setter
    def code(self, new_code):
        assert isinstance(new_code, str) and len(new_code) == 4, 'Номер должен состоять из 4 цифр'
        self.__code = new_code

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, new_card_number):
        assert isinstance(new_card_number, str) and len(new_card_number) == 16, "Номер карты должен состоять из 16 цифр"
        self.__card_number = new_card_number

    



card = Terminal('1234567890123456', '1234')

card.put('1234', 1000)
card.put('1234', 500)

card.get_money('1234', 300)
card.get_money('1234', 800)

card.check_balance()

print(card.card_number)

print(card.code)
