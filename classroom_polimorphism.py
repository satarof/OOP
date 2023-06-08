"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. Если image True, то выдается сообщение “I am sending a text … with some image ”, если  False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""
# писать код здесь

# class WhatsApp:
#     def __init__(self, number:int):
#         self.number = number

#     def send(self, text):
#         self.text = text
#         return f'I am sending a text {text}'

# class SnapChat:
#     def __init__(self, number:int):
#         self.number = number

#     def send(self, image, text):
#         if image == True:
#             return f'I am sending a text {text} with some image '
#         else:
#             return f'I am sending a text {text} without image'


# class Telegram:
#     def __init__(self, number:int, username):
#         self.username = username
#         self.number = number

#     def send(self, voice_message):

#         return f'I am sending a voice message {voice_message}'
    

# whatsapp  = WhatsApp(123456)
# print(whatsapp.send('hello')  )   

# snapchat = SnapChat(654321)
# print(snapchat.send(image = True, text = 'look at my photo'))

# telegram = Telegram(987654, 'tim')
# print(telegram.send(voice_message='assalamualekum'))




"""
2) Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""
# писать код здесь

class A:
    def count(self, word:str):
        vowels = ['a', 'e', 'i', 'o', 'u']
        self.count = 0
        for letter in word: 
            if letter.lower() in vowels:
                self.count += 1
        return self.count


class B:
    def count(self, word:str):
        consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S' , 'T', 'V', 'W', 'X', 'Y', 'Z']
        self.count = 0
        for letter in word: 
            if letter.upper() in consonant:
                self.count += 1
        return self.count

obj = B()
obj1 = A()
print(obj.count('Timur'))
print(obj1.count('Temirlan'))