class Man:
    def __init__(self, sex, year, ):
        self.sex = sex
        self.year = year

    # Python
    # 中类内部定义的实例方法，第一个参数必须是
    # self，这是语法强制要求。

    def c1(self):
        print(f"{self.sex}-{self.year}")

    # c2=Man('男','18')
    # print(c2.sex) #男
    # c2.c1()   #男-18

    # print(c2)     #会直接打印内存地址要想不显示则需要用到__str__魔法函数，str函数以后只要有print()则会自动调用str函数，并且打印str函数的返回值
    # <__main__.Man object at 0x000001CA97871A90>

    def __str__(self):  # 要有return
        return f'这个人的性别是{self.sex},这个人的年龄{self.year}'


# def __del__(self): 记录日志，删除信息

c2 = Man('男', '18')
print(c2)

# 类：通用模板，定义一类事物共有特征与功能；
# 对象：根据模板创建的独立、具体个体，拥有专属数据；
# 作用：代码复用、逻辑打包、贴合现实思维，是大型项目、AI、爬虫、GUI 程序的核心编程方式



 #  ---------------------------------类属性和对象（成员属性）-------------------------------------
# 定义Person类
class Person:
    # 类属性（所有对象共享）
    species = "人类"

    def __init__(self, name):
        # 对象属性/实例属性（每个对象独立独有）
        self.name = name

# 1. 创建2个对象
p1 = Person('张三')
p2 = Person('李四')

# 访问【对象属性】
print(p1.name)  # 输出 张三
print(p2.name)  # 输出 李四

# 访问【类属性】两种方式
print(p1.species)    # 通过对象访问类属性
print(Person.species) # 通过类直接访问类属性

# ---------------- 修改属性 ----------------
# 修改对象属性：只影响p1自己，不影响p2、不影响类
p1.name = 'zhangsan'
print(p1.name) # 输出 zhangsan

# 正确修改类属性：必须用【类名.属性】，所有对象同步生效
Person.species = '人科'
print(p1.species) # 输出 人科

# 易错点：对象.species = xxx 不是修改类属性！
# 只是给p1新增了一个同名的【对象属性】，屏蔽了原来的类属性
p1.species = '人属'
print(p1.species) # 输出 人属