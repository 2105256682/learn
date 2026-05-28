# 判断是否成年
age = int(input("please input your age:"))
if age >= 18:
    print(f"我已经成年了是{age}岁")
else:
    print("你还是未成年")
# 示例输入：19
# 运行结果：我已经成年了是19岁


# 定义变量 num = 12，用 if...else 判断数字是奇数还是偶数，并输出结果。
num = 12
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
# 运行结果：12是偶数


# 成绩判断：score = 72，规则：≥90 优秀、≥80 良好、≥60 及格、<60 不及格，使用if-elif-else实现
score = 72
if score >= 90:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
else:
    print("不及格")
# 运行结果：及格


# 多条件：定义 age=25、is_student=True，使用逻辑运算符，同时满足年龄小于 30 且是学生则打印「符合优惠条件」。
a = 25
is_student = True
if a < 30 and is_student:
    print("符合优惠条件")
else:
    print("不符合")
# 运行结果：符合优惠条件


# 月份判季节：输入变量 month = 2，规则：
# 3-5 月：春季
# 6-8 月：夏季
# 9-11 月：秋季
# 12、1、2 月：冬季
# 超出 1-12 则打印「无效月份」。
month = 2
if 3 <= month <= 5:
    print("春季")
elif 6 <= month <= 8:
    print("夏季")
elif 9 <= month <= 11:
    print("秋季")
elif month == 12 or 1 <= month <= 2:
    print("冬季")
else:
    print("无效月份")
# 运行结果：冬季


# 三元表达式：变量 a=35，b=56，用一行三元代码取出两个数中较小的值并打印。
m = 35
b = 56
res = m if m < b else b
print(res)
# 运行结果：35


# 成员运算符：列表 lst = ["苹果","香蕉","橙子"]，判断字符串 "香蕉" 是否在列表中，在则打印「存在该水果」。
lst = ["苹果", "香蕉", "橙子"]
if "香蕉" in lst:
    print("存在该水果")
# 运行结果：存在该水果


# or 逻辑运算：hour = 23，规则：时间小于 6 或 大于 22，打印「夜间时段」。
hour = 23
if hour < 6 or hour > 22:
    print("夜间时段")
# 运行结果：夜间时段
