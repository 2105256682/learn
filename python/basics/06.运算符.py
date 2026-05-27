# 1.算数运算符
a = 10
b = 3
# 1. + 加
print(a + b)  # 13
# 2. - 减
print(a - b)  # 7
# 3. * 乘
print(a * b)  # 30
# 4. / 除（结果一定是浮点数）
print(a / b)  # 3.3333333333333335
# 5. // 整除（向下取整）
print(a // b)  # 3
print(-a // b)  # -4 （注意负数向下取整）
# 6. % 取余（求模）
print(a % b)  # 1
# 7. ** 幂运算
print(a ** b)  # 1000

# 2.比较运算符
x = 5
y = 8
print(x == y)  # False  等于
print(x != y)  # True   不等于
print(x > y)  # False  大于
print(x < y)  # True   小于
print(x >= y)  # False  大于等于
print(x <= y)  # True   小于等于
# 链式比较（Python 特有）
print(1 < x < 10)  # True

# 3.赋值运算符
num = 20
num += 5
print(num)  # 25
num -= 3
print(num)  # 22
num *= 2
print(num)  # 44
num /= 4
print(num)  # 11.0
num //= 3
print(num)  # 3.0
num %= 2
print(num)  # 1.0
num **= 3
print(num)  # 1.0

# 4.逻辑运算符
p = True
q = False

print(p and q)  # False  逻辑与
print(p or q)  # True   逻辑或
print(not p)  # False  逻辑非
# and：全真才真，一假则假
# or：一真则真，全假才假
# not：对布尔值做反转

# 5.位运算符
s = 60  # 二进制：00111100
t = 13  # 二进制：00001101

print(s & t)  # 12   按位与：对应二进制位都为1，结果才是1
print(s | t)  # 61   按位或：对应二进制位有一个为1，结果就是1
print(s ^ t)  # 49   按位异或：对应二进制位不同则为1，相同则为0
print(~s)  # -61  按位取反：所有二进制位0变1、1变0（Python带符号运算）
print(s << 2)  # 240  左移：二进制整体向左移2位，等价 ×2²
print(s >> 2)  # 15   右移：二进制整体向右移2位，等价 ÷2²

#二进制（十进制转二进制）
# 规则：不断除以 2，记录余数，最后从下往上读余数
# 示例 1：把 60 转二进制
# plaintext
# 60 ÷ 2 = 30    余 0
# 30 ÷ 2 = 15    余 0
# 15 ÷ 2 = 7     余 1
# 7  ÷ 2 = 3     余 1
# 3  ÷ 2 = 1     余 1
# 1  ÷ 2 = 0     余 1
# 停止计算，从最后一个余数往第一个读：
# 1 1 1 1 0 0 → 简写：111100
# 补足 8 位（编程常用 8 位对齐）：00111100

#二进制转十进制
# 核心口诀
# 从右往左，依次 × 1、2、4、8、16、32…… 然后全部加起来！
# 举个例子：二进制 111100 → 十进制是多少？
# 第一步：把数字从右往左标权重
# 权重固定是：1, 2, 4, 8, 16, 32（都是 2 的次方）
# 二进制数：1 1 1 1 0 0
# 位置权重：32 16 8 4 2 1
# 第二步：把 1 下面的权重加起来，0 跳过
# plaintext
# 1 → 32
# 1 → 16
# 1 → 8
# 1 → 4
# 0 → 跳过
# 0 → 跳过
# 32 + 16 + 8 + 4 = 60
# 所以：111100 二进制 = 60 十进制


# 6.成员运算符
lst = [1, 2, 3, 4]
str1 = "hello"

print(2 in lst)  # True
print(5 not in lst)  # True
print("h" in str1)  # True

# 7.身份运算符
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
obj3 = obj1

print(obj1 is obj2)  # False
print(obj1 is not obj2)  # True
print(obj1 is obj3)  # True
