import random  # 随机数模块

# 模块  math
# 第一种
import math

# 模块名.函数（对象）
print(math.log2(8))
print(math.log(8, 2))

# 第二种: from 模块名字 import *
from math import *

# 优点：模块名长的时候使用可以直接使用函数
# 缺点：与定义函数相冲突概率大
print(log2(8))

# 第三种：精确导入
from math import log2, log10

print(log2(8))
print(log10(100))

# 第四种
import multiprocessing as mp

print(mp.current_process())

# 第五种
from math import log2 as lg2

print(lg2(8))

# 2模块的限制
# 前提：使用的是from ···import *
#  __all__ =['my_sum']   ,声明当前模块只能调用my_sum函数


# 测试模块,测试内容放if __name__ == '__main__': 下里面的代码 = 工具自带的测试 Demo
# if __name__ == '__main__'
# 测试内容

# python包创建包会自动产生一个__inin__.py文件，用来控制包导入行为

# 3导入包中的模块
# import 包名.模块名   ，from 包名.模块名 import *


# 4安装第三方库
# 一、安装命令
# pip install 库名字 # 安装最新版本
# pip install 库名字==1.0.4 # 指定版本安装
#查看已装库：pip list；更新库：pip install -U 库名；卸载库：pip uninstall -y 库名
# pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple/
# 二、镜像源说明
# 注意：-i 指定 pip 镜像源，下载速度更快；默认是 Python 国外官方源，下载速度慢。
# 国内 pip 镜像源列表
# 中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣：https://pypi.douban.com/simple/
# 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
# 阿里云：http://mirrors.aliyun.com/pypi/simple/
# 三、查看已安装库命令
# pip list：查看已安装的第三方库
# pip list -o：对比查看可更新的库版本
