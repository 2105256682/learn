# Python 基础 - 第1天笔记

> 日期：2026-05-26

---

## 01. 注释

注释不会被执行，用来解释代码。

### 单行注释
```python
# 这是单行注释
# print("这行不会执行")
```

### 多行注释
```python
"""
这是多行注释
可以写很多行
"""

'''
这也是多行注释
两种引号都可以
'''
```

---

## 02. PyCharm 常用快捷键

| 快捷键 | 作用 |
|---|---|
| `Ctrl + Y` | 删除当前行 |
| `Ctrl + Alt + Enter` | 向上换行 |
| `Ctrl + Shift + I` | 查看官方文档 |
| `Ctrl + /` | 注释 / 取消注释 |
| `Ctrl + D` | 复制当前行 |
| `Shift + Enter` | 快速向下换行 |
| `Ctrl + Shift + 方向键` | 移动当前行 |
| `Ctrl + Alt + L` | 格式化代码 |

---

## 03. 变量

### 基本赋值
```python
num1 = 5
my_name = 'wu'
age = 19
```

### 多变量赋值
```python
# 两个变量赋同一个值
name01 = name02 = '孙悟空'

# 一行赋多个值
a1, a2, a3 = 100, 200, 300
```

### 变量类型

| 类型 | 英文 | 例子 |
|---|---|---|
| 整数 | int | `num = 100` |
| 小数 | float | `num = 0.12` |
| 布尔 | bool | `b = True / False` |
| 字符串 | str | `s = 'abc'` |

```python
# 查看变量类型
print(type(num01))   # <class 'int'>

# 明确指定类型（类型注解）
num: float = 9.8
```

---

## 04. 输入 input()

- `input()` 获取到的内容**永远是字符串类型**
- 需要数字时要手动转换类型

```python
name = input('请输入你的名字')
print(name)
print(type(name))   # <class 'str'>

# 类型转换：字符串 → 整数
age = input('请输入你的年龄')
age = int(age)
print(type(age))    # <class 'int'>
```

---

## 05. 输出格式化 print()

### 基本格式化
```python
my_name = '张三'
my_age = 18
my_city = 'hubei'

# %s 字符串占位，%d 整数占位
print('我的名字是%s' % my_name)
print('我的名字是%s, 我的年龄是%d, 我所在的城市%s' % (my_name, my_age, my_city))
```

### 数字格式化

| 格式 | 含义 | 例子 |
|---|---|---|
| `%d` | 整数 | `'%d' % 8923` → `8923` |
| `%5d` | 整数，宽度5位（右对齐） | `'%5d' % 8923` → ` 8923` |
| `%.1f` | 小数保留1位 | `'%.1f' % 1.71` → `1.7` |
| `%.2f` | 小数保留2位 | `'%.2f' % 22.345` → `22.35`（不准确）|

### 精确四舍五入（用 Decimal）

> `%.2f` 的四舍五入在某些情况下不准确，精确场景用 `Decimal`

```python
from decimal import Decimal

num = 22.345
result = Decimal(str(num)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP')
print(result)   # 22.35
```

---

## 今日总结

- 注释：`#` 单行，`"""` 或 `'''` 多行
- 变量：直接赋值，`type()` 查类型
- 输入：`input()` 返回的是字符串，需要数字要 `int()` 转换
- 输出：`%s` 字符串、`%d` 整数、`%.2f` 小数，精确四舍五入用 `Decimal`
