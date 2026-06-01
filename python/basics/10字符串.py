# ===================== 一、字符串定义 =====================
# 1. 字符串三种表示方式
s1 = 'hello, world!'  # 单行字符串
s2 = "你好，世界！❤️"  # 中文+表情
s3 = '''hello,                           # 多行字符串
wonderful
world!'''
print(s1)  # 结果：hello, world!
print(s2)  # 结果：你好，世界！❤️
print(s3)  # 结果：hello,\nwonderful\nworld!

# 2. 转义字符
s4 = '\'hello, world!\''  # 转义单引号
s5 = '\\hello, world!\\'  # 转义反斜杠
print(s4)  # 结果：'hello, world!'
print(s5)  # 结果：\hello, world!\

# 3. 原始字符串（取消转义）
s6 = '\it \is \time \to \read \now'  # 普通字符串（含转义）
s7 = r'\it \is \time \to \read \now'  # 原始字符串（无转义）
print(s6)  # 结果：it is ime o ead now
print(s7)  # 结果：\it \is \time \to \read \now

# 4. 特殊编码字符（八进制/十六进制/Unicode）
s8 = '\141\142\143\x61\x62\x63'  # a b c
s9 = '\u9a86\u660a'  # 骆昊
print(s8)  # 结果：abcabc
print(s9)  # 结果：骆昊

# ===================== 二、字符串运算 =====================
# 1. 拼接 + 重复
s10 = 'hello' + ', ' + 'world'  # 字符串拼接
s11 = '!' * 3  # 字符串重复
print(s10)  # 结果：hello, world
print(s11)  # 结果：!!!

s10 += s11  # 复合赋值
print(s10)  # 结果：hello, world!!!
s10 *= 2
print(s10)  # 结果：hello, world!!!hello, world!!!

# 2. 比较运算（按Unicode编码比较）
s12 = 'a whole new world'
s13 = 'hello world'
print(s12 == s13)  # 结果：False
print(ord('a'))  # 97
print(ord('h'))  # 104
print(s12 < s13)  # 结果：True
print(ord('骆'))  # 结果：39558  ord获取编码数
print(ord('昊'))  # 结果：26122
# Python 比较字符串大小，是按「第一个不同字符」的 Unicode 编码值来比！谁的编码数字小，谁就小。


# 3. 成员运算
s14 = 'hello, world'
s15 = 'goodbye, world'
print('wo' in s14)  # 结果：True
print('wo' not in s15)  # 结果：False

# 4. 获取长度
s16 = 'hello, world'
print(len(s16))  # 结果：12

# 5. 索引与切片
s17 = 'abc123456'
n = len(s17)
print(s17[0], s17[-n])  # 结果：a  a
print(s17[2:5])  # 结果：c12
print(s17[::2])  # 结果：ac246
print(s17[::-1])  # 结果：654321cba

# ===================== 三、字符串遍历 =====================
s18 = 'hello'
# 方式1：索引遍历
for i in range(len(s18)):
    print(s18[i])  # 逐行输出：h e l l o

# 方式2：直接遍历（推荐）
for elem in s18:
    print(elem)  # 逐行输出：h e l l o

# ===================== 四、字符串常用方法 =====================
# 1. 大小写转换
s19 = 'hello, world!'
print(s19.capitalize())  # 结果：Hello, world!
print(s19.title())  # 结果：Hello, World!
print(s19.upper())  # 结果：HELLO, WORLD!

s20 = 'GOODBYE'
print(s20.lower())  # 结果：goodbye

# 2. 查找子串
s21 = 'hello, world!'
print(s21.find('or'))  # 结果：8
print(s21.find('or', 9))  # 结果：-1
print(s21.rfind('o'))  # 结果：7

# 3. 字符串判断
s22 = 'hello, world!'
print(s22.startswith('hel'))  # 结果：True
print(s22.endswith('!'))  # 结果：True

s23 = 'abc123'
print(s23.isdigit())  # 结果：False
print(s23.isalpha())  # 结果：False
print(s23.isalnum())  # 结果：True

# 4. 对齐与格式化
s24 = 'hello, world'
print(s24.center(20, '*'))  # 结果：****hello, world****
print(s24.rjust(20))  # 结果：         hello, world
print('33'.zfill(5))  # 结果：00033

a, b = 321, 123
print(f'{a} * {b} = {a * b}')  # 结果：321 * 123 = 39483

# 5. 修剪操作
s25 = '   test@126.com  '
print(s25.strip())  # 结果：test@126.com

s26 = '~你好，世界~'
print(s26.lstrip('~'))  # 结果：你好，世界~
print(s26.rstrip('~'))  # 结果：~你好，世界

# 6. 替换操作
s27 = 'hello, good world'
print(s27.replace('o', '@'))  # 结果：hell@, g@@d w@rld
print(s27.replace('o', '@', 1))  # 结果：hell@, good world

# 7. 拆分与合并
s28 = 'I love you'
words = s28.split()
print(words)  # 结果：['I', 'love', 'you']
print('~'.join(words))  # 结果：I~love~you

s29 = 'I#love#you#so'
print(s29.split('#', 2))  # 结果：['I', 'love', 'you#so']

# 8. 编码与解码
s30 = '骆昊'
b1 = s30.encode('utf-8')
b2 = s30.encode('gbk')
print(b1)  # 结果：b'\xe9\xaa\x86\xe6\x98\x8a'
print(b2)  # 结果：b'\xc2\xe6\xea\xbb'
print(b1.decode('utf-8'))  # 结果：骆昊
print(b2.decode('gbk'))  # 结果：骆昊
