# 1.单行注释 #
# print("hello world")

# 2.多行注释 ("""  """)    或者   ('''   ''')
"""
print("hello world")
print("hello world")
print("hello world")
"""

print("hello world")

'''
print("hello world")'
print("hello world")
print("hello world")
print("hello world")
'''
# 二、Debug 调试
# 1、打断点
# 一个断点标记了一个代码行，当 Pycharm 运行到该行代码时会将程序暂时挂起。断点会将对应的代码行标记为红色，取消断点的操作也很简单，在同样位置再次单击即可。一定要 debug 运行才生效。
# 注意：断点一般打在有报错嫌疑的代码前面，或者是：抛出异常的代码前面。而且可以打多个断点。
# 2、Debug 操作
# PyCharm 执行 debug 流程：
# PyCharm 开始运行，并在断点处暂停
# 断点所在代码行变蓝，意味着 PyCharm 程序进程已经到达断点处，但尚未执行断点所标记的代码。
# Debug tool window 窗口出现，显示当前重要调试信息，并允许用户对调试进程进行更改。
# 调试工具栏快捷键功能说明
# show execution point (F10)：显示当前所有断点
# step over (F8) 单步调试
# 若函数 A 内存在子函数 a 时，不会进入子函数 a 内执行单步调试，而是把子函数 a 当作一个整体，一步执行完
# step into (F7) 单步调试
# 若函数 A 内存在子函数 a 时，会进入子函数 a 内执行单步调试。
# step into my code (Alt + Shift +F7)：执行下一行但忽略 libraries（导入库的语句）
# force step into (Alt + Shift +F7)：执行下一行，忽略 lib 和构造对象等底层代码
# step out (Shift+F8)：当目前执行在子函数 a 中时，选择该调试操作可以直接跳出子函数 a，而不用继续执行子函数 a 中的剩余代码，并返回上一层函数。
# run to cursor (Alt +F9)：直接跳到光标所在行 / 下一个断点
