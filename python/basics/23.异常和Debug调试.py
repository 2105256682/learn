# 一、多分支 try-except 语法模板
# python
# 运行
# try:
#     可能发生错误的代码
# except 异常类型1:
#     如果捕获到该异常类型1执行的代码
# except 异常类型2:
#     如果捕获到该异常类型2执行的代码
# ……
# 补充说明：
# 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
# 二、try 语句工作原理
# 首先，执行 try 子句（try 和 except 关键字之间的（多行）语句）。
# 如果没有触发异常，则跳过 except 子句，try 语句执行完毕。
# 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，然后跳到 try/except 代码块之后继续执行。
# 如果发生的异常与 except 子句中指定的异常不匹配，则它会被传递到外部的 try 语句中；如果没有找到处理程序，则它是一个 未处理异常 且执行将终止。
try:
    f = open('abc.txt')
    s = f.readline()
    num = int(s.strip())
    print(num)
except Exception as err:  # Exception是所有异常的父类，可以说用这个可以直接捕获所有异常
    print(err)

# 要捕获详细信息要导入traceback模块，并且except Exception as err:就不用命名,使用traceback.format_exc()
# import traceback
# except Exception:
# print(traceback.format_exc())



# 2、强制抛出异常
# raise 语句支持强制触发指定的异常。比如：如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 raise 语句重新触发异常。
# 示例代码：
# python
# 运行
# >>> try:
# ...     raise NameError('HiThere')
# ... except NameError:
# ...     print('An exception flew by!')
# ...


# 3、异常中的 else
# else 表示的是如果没有异常要执行的代码。
# python
# 运行
# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:
#     print('我是else，是没有异常的时候执行的代码')



# 4、Finally 语句
# finally 表示的是无论是否异常都要执行的代码，例如关闭文件。一般都是做一些清理工作。
# python
# 运行
# try:
#     f = open('test.txt', 'r')
# except Exception as result:
#     f = open('test.txt', 'w')
# else:
#     print('没有异常，真开心')
# finally:
#     f.close()


# 1. 定义自定义异常类
class PasswordToShortError(Exception):
    """
    自定义的异常，密码太短了
    """
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 打印异常对象，就会打印__str__函数的返回值
    def __str__(self):
        return f'你输入的密码长度是{self.length}，密码不能少于{self.min_len}'

# 2. 封装密码输入函数，校验并主动抛出自定义异常
def input_password():
    pwd = input('请输入你的密码:')
    # 规定密码的长度不能少于6个字符
    if len(pwd) < 6:
        raise PasswordToShortError(len(pwd), min_len=6)

# 3. 程序入口，try-except捕获自定义异常
if __name__ == '__main__':
    try:
        input_password()
    except Exception as err:
        print(err)