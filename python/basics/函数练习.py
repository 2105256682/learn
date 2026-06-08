# 1. 函数基础
# 定义一个函数 say_hello()，打印 Hello Python，并调用它。
def say_hello():
    print("hello")


say_hello()


# 2. 带参数函数
# 写一个函数 add(a, b)，返回两个数的和。
def add(a, b):
    return a + b


print(add(1, 2))


# 3. 默认参数
# 写函数 power(num, n=2)，返回 num 的 n 次方（默认平方）。
def power(num, n=2):
    return num ** n


print(power(2, 3))


# 4. 递归求和
# 用递归实现：求 1 + 2 + 3 + ... + n 的和。
def my_sum(m: int) -> int:
    if m == 1:
        return 1
    return m + my_sum(m - 1)


print(my_sum(100))


# 5. 递归求斐波那契
# 用递归写出函数 fib(n)，返回第 n 个斐波那契数。
# 规则：fib(1)=1, fib(2)=1, fib(n)=fib(n-1)+fib(n-2)
def fib(b):
    if b == 1 or b == 2:
        return 1
    return fib(b - 1) + fib(b - 2)


print(fib(10))


# 6. 递归求阶乘（完善版）
# 写递归函数 factorial(n)，计算 n!，并处理 n<0 的情况。
def factorial(n: int) -> int:
    if n <= 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# 7. 递归反转字符串
# 写函数 reverse_str(s)，用递归返回字符串的倒序。
# 例：reverse_str('abc') → 'cba'
def revrerse_str(s: str) -> str:
    if len(s) <= 1:
        return s
    return revrerse_str(s[1:]) + s[0]


# print(revrerse_str("hello"))
#
# 8. 最简单装饰器
# 写一个装饰器，让任何函数执行前都打印 函数开始执行，执行后打印 函数执行完毕。
def demo_decorator(func):
    def wrapper(*args, **kwargs):  # 装饰器99%都要带参数，不确定别是定义的函数是否有参数
        print("函数开始执行")
        # 调用原函数
        res = func(*args, **kwargs)
        print("函数执行完毕")
        return res

    return wrapper


# 测试
@demo_decorator
def test():
    print("我是原函数逻辑")


test()

# 9. 计时装饰器（必做）
# 写一个计时装饰器 timer，可以装饰任何函数，自动打印函数执行时间。
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行耗时: {end - start:.2f} 秒")
        return result

    return wrapper


@timer
def sleep_func():
    time.sleep(1)


sleep_func()
#
# 12. 使用 map + Lambda
# 把列表 [1,2,3,4,5] 所有元素平方，一行代码完成。
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

# 13. 使用 filter + Lambda
# 过滤出列表 [1,3,5,7,9,10,12] 中的偶数。
print(list(filter(lambda x: x % 2 == 0, [1, 3, 5, 7, 9, 10, 12])))

# 14. sorted + 自定义 key
# 对列表 ['apple', 'banana', 'cherry', 'date'] 按字符串长度从小到大排序。
words = ['apple', 'banana', 'cherry', 'date']
print(sorted(words, key=len))  # key来决定按长度排布而非字母

# 15. 偏函数练习
# 使用 functools.partial 创建一个函数 bin2int，专门把二进制字符串转成十进制整数。
from functools import partial
q = partial(int, base=2)
print(q('101'))  #5
print(q('1010')) # 10