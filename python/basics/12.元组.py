# ====================== 1. 元组基础定义、类型查看、len() ======================
# 多元素元组
t_create1 = (35, 12, 98)
t_create2 = ('骆昊', 45, True, '四川成都')

print(type(t_create1))  # <class 'tuple'>
print(type(t_create2))  # <class 'tuple'>
print(len(t_create1))   # 3
print(len(t_create2))   # 4

print("-" * 50)

# ====================== 2. 空元组、单元素元组特殊语法 ======================
t_empty = ()
t_wrong_str = ('hello')
t_wrong_int = (100)
t_single_str = ('hello', )
t_single_int = (100, )

print(type(t_empty))      # <class 'tuple'>
print(type(t_wrong_str))  # <class 'str'>
print(type(t_wrong_int))  # <class 'int'>
print(type(t_single_str)) # <class 'tuple'>
print(type(t_single_int)) # <class 'tuple'>

print("-" * 50)

# ====================== 3. 索引、切片操作 ======================
t_index_slice = ('骆昊', 45, True, '四川成都')
# 索引
print(t_index_slice[0])    # 骆昊
print(t_index_slice[2])    # True
print(t_index_slice[-1])   # 四川成都
# 切片
print(t_index_slice[:2])   # ('骆昊', 45)
print(t_index_slice[::3])  # ('骆昊', '四川成都')

print("-" * 50)

# ====================== 4. 元组遍历 for循环 ======================
t_for_demo = (35, 12, 98)
# 方式1：直接遍历元素
print("直接遍历元素：")
for elem in t_for_demo:
    print(elem)

# 方式2：通过索引遍历
t_for_index = ('Python', 'Java', 'C++')
print("\n通过索引遍历：")
for index in range(len(t_for_index)):
    print(f'下标{index}：{t_for_index[index]}')

print("-" * 50)

# ====================== 5. 成员运算 in / not in ======================
t_member_demo = (35, 12, 98)
print(12 in t_member_demo)         # True
print(99 in t_member_demo)         # False
print('Hao' not in t_member_demo)  # True

print("-" * 50)

# ====================== 6. 拼接+、重复*、比较运算 ======================
t_add1 = (35, 12, 98)
t_add2 = ('骆昊', 45, True, '四川成都')
t_concat = t_add1 + t_add2
print(t_concat)  # (35, 12, 98, '骆昊', 45, True, '四川成都')

t_mul_demo = (1, 2)
print(t_mul_demo * 3)  # (1, 2, 1, 2, 1, 2)

t_cmp_a = (35, 12, 98)
t_cmp_b = (35, 11, 99)
print(t_cmp_a == t_cmp_b)            # False
print(t_cmp_a >= t_cmp_b)            # True
print(t_cmp_a <= (35, 11, 99))       # False

print("-" * 50)

# ====================== 7. index()、count() 元组内置方法 ======================
t_func_index = (35, 12, 35, 98)
print(t_func_index.index(35)) # 0

t_func_count = (35, 12, 35, 98, 35)
print(t_func_count.count(35)) # 3
print(t_func_count.count(12)) # 1

print("-" * 50)

# ====================== 8. 打包操作 ======================
t_pack_demo = 1, 10, 100
print(type(t_pack_demo))  # <class 'tuple'>
print(t_pack_demo)        # (1, 10, 100)

print("-" * 50)

# ====================== 9. 基础解包 ======================
t_unpack_base = (1, 10, 100)
i, j, k = t_unpack_base
print(i, j, k)  # 1 10 100

print("-" * 50)

# ====================== 10. 星号*解包表达式 ======================
t_star_unpack = (1, 10, 100, 1000)
i1, j1, *k1 = t_star_unpack
print(i1, j1, k1)        # 1 10 [100, 1000]

i2, *j2, k2 = t_star_unpack
print(i2, j2, k2)        # 1 [10, 100] 1000

*i3, j3, k3 = t_star_unpack
print(i3, j3, k3)        # [1, 10] 100 1000

i4, j4, k4, *l4 = t_star_unpack
print(i4, j4, k4, l4)     # 1 10 100 [1000]

i5, j5, k5, l5, *m5 = t_star_unpack
print(i5, j5, k5, l5, m5)  # 1 10 100 1000 []

print("-" * 50)

# ====================== 11. 列表/range/字符串通用解包 ======================
print("range解包：")
ra, rb, *rc = range(1, 10)
print(ra, rb, rc)

print("\n列表解包：")
la, lb, lc = [1, 10, 100]
print(la, lb, lc)

print("\n字符串解包：")
sa, *sb, sc = 'hello'
print(sa, sb, sc)

print("-" * 50)

# ====================== 12. 元组交换变量 ======================
# 两个变量交换
num_a = 100
num_b = 200
num_a, num_b = num_b, num_a
print("两变量交换：", num_a, num_b)

# 三个变量交换
x, y, z = 1, 2, 3
x, y, z = y, z, x
print("三变量交换：", x, y, z)

print("-" * 50)

# ====================== 13. 列表、元组互相转换 ======================
tuple_to_list = ('骆昊', 45, True, '四川成都')
res_list = list(tuple_to_list)
print("元组转列表：", res_list)

list_to_tuple = ['apple', 'banana', 'orange']
res_tuple = tuple(list_to_tuple)
print("列表转元组：", res_tuple)

print("-" * 50)

# ====================== 14. 性能对比 timeit 代码 ======================
import timeit
time_list = timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000)
time_tuple = timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000)
print(f'列表创建耗时：{time_list:.3f} 秒')
print(f'元组创建耗时：{time_tuple:.3f} 秒')