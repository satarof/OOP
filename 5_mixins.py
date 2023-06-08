'=======================================Mixins======================================'
# миксины - классы помощники, которые будут использоваться для наследовния. от миксинов не создаютмя объекты

class FlyMixin:
    def fly(self):
        print('я могу леать')

class WalMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def  swim(self):
        print('я могу плавать')

class Human(WalMixin, SwimMixin):
    name = 'Человек'

    def talk(self):
        print('я могу говорить')

class fish(SwimMixin):
    name = 'рыба'

class duck(WalMixin,SwimMixin,FlyMixin):
    name = 'утка'

objs = [Human(), duck(), fish()]
for obj in objs:
    print(obj.name)

    attrs = ['fly', 'walk', 'talk', 'swim']
    for attr in attrs:
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            method()

obj1 = Human()
setattr(obj1, 'new_attr' , 'hello_world')
print(obj1.new_attr)

# hassattr - функция, которая принимает объкт и название аттрибута. Возвращает True, если у объекта есть такой атрибут (метод)
# getattr - функция, которая принимает объкт и название аттрибута. Возвращает  значение атрибута, либо метода
# setattr - функция, которая принимает объкт и название аттрибута и его значение. Добавляет в объект новый атрибут или перезапишет в одноименный атрибут
