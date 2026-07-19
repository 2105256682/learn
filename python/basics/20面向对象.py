# 五、面向对象三大特性
# 封装
# 将属性和方法书写到类的里面的操作即为封装
# 封装可以为属性和方法添加私有权限
# 继承
# 子类默认继承父类的所有属性和方法
# 子类可以重写父类属性和方法
# 多态
# 传入不同的对象，产生不同的结果


# 继承函数
class father:
    def __init__(self, name):
        self.name = name

    def man(self, aihao):
        res = f"{self.name}的爱好是{aihao}"
        return res


class son(father):
    # 子类重写构造，统一初始化姓名+年龄
    def __init__(self, name, age):
        # 在构造函数中调用父类构造，只在这里用super()
        super().__init__(name)
        self.age = age

    def old(self):
        # 仅读取已有属性，不需要传name
        print(f"{self.name}的年龄是{self.age}岁")


# 父类测试
f1 = father("小明")
c1 = f1.man("钓鱼")
print(c1)

# 创建子类对象，一次性传入姓名、年龄
c2 = son("张三", 18)
# 调用子类方法，无需传参
c2.old()

# 子类也能调用继承的父类方法
print(c2.man("打游戏"))


# 多态 ,传入不同的对象，产生不同的结果
class Animal:

    def say(self):
        pass


class Dog(Animal):

    def say(self):
        print('旺旺')


class Cat(Animal):
    def say(self):
        print('喵喵')


def test(obj):
    obj.say()


d = Dog()
c = Cat()

test(d)
test(c)
