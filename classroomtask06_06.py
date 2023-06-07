"""
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов, изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык. При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding, в классе Python он должен выдавать вам строку “I am Python student. I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала. После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”
"""
# писать код здесь

import random


class Languages:
    quantity_students = 0
    def __init__(self):
        Languages.quantity_students += 1
            

class Python(Languages):
    student = 0
  
    def __str__(self) -> str:
        return 'Python'

    def __init__(self):
        super().__init__()
        Python.student += 1
    
    def coding(self):
        return f'I am Python student. I am coding now'
    
class JavaScript(Languages):
    student = 0

    def __str__(self) -> str:
        return 'JavaScript'

    def __init__(self):
        super().__init__()
        JavaScript.student += 1

    def coding(self):
        return f'I am JavaScript student. I am coding now'
    


def guess_student():
    students = [Python(), JavaScript()]
    select_student = random.choice(students)
    # print(str(select_student))
    guess_st = input('Угадайте выбранного студента "Python" или "JavaScript": ')

    if isinstance(select_student, Python) and guess_st.lower() == 'python':
        print(f'{studentpy.coding()} \nGood job!')

    elif isinstance(select_student, JavaScript)  and guess_st.lower() == 'javascript':
        print(f'{studentJS.coding()} \nGood job!')

    else:
        print(f'No bueno :( \nкомпьютер выбрал: {select_student}')

studentpy = Python()
studentpy1 = Python()
studentpy2 = Python()
studentpy3 = Python()
studentpy4 = Python()
studentpy5 = Python()


studentJS = JavaScript()
studentJS1 = JavaScript()
studentJS2 = JavaScript()
studentJS3 = JavaScript()
studentJS4 = JavaScript()


guess_student()
print(f' Общее количество студентов {Languages.quantity_students}')
print(f' Количество студентов Python {Python.student}')
print(f' Количество студентов JS {JavaScript.student}')



"""
2) Создайте свой класс MyList, который наследуется от list. Переопределите метод списка insert(), который обычно принимает первым аргументом индекс, а вторым - элемент. В своем классе MyList переопределите этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс
"""
class MyList(list):
    def insert(self, index, element):
        return super().insert(element, index)
list = MyList([1,2,3,4,5])
print(list)
list.insert(1,3)
print(list)
        