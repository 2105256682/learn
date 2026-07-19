class Animal:
    __name__ = "动物"  # 私有属性（类属性）

    def __init__(self, color):
        self.__color = color  # 私有属性

    def __run(self):
        print("动物跑起来了")

    def say(self):
        print('动物喊叫')
        print(self.__color)

    def set_color(self, new_color):  # 通过提供一个set函数来修改私有属性
        self.__color = new_color

    def get_color(self):  # 访问
        return self.__color


class Dog(Animal):
    pass


d = Dog('red')
# d.__run()   #报错
d.set_color('blue')
d.say()
