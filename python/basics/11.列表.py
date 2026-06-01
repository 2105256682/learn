# 1. 纯数字列表
items1 = [35, 12, 99, 68, 55, 35, 87]
# 2. 字符串列表
items2 = ['Python', 'Java', 'Go', 'Kotlin']
# 3. 混合类型列表（不推荐日常使用）
items3 = [100, 12.3, 'Python', True]

print(items1)  # 输出：[35, 12, 99, 68, 55, 35, 87]
# 解释：列表允许重复数字35
print(items2)  # 输出：['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # 输出：[100, 12.3, 'Python', True]
# 解释：同时包含int、float、字符串、布尔值四种类型


# range整数序列转列表
items4 = list(range(1, 10))
# 字符串（字符序列）转列表，每个字符成为列表元素
items5 = list('hello')

print(items4)  # 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 解释：range(1,10)生成1~9整数，list转为列表
print(items5)  # 输出：['h', 'e', 'l', 'l', 'o']
# 解释：字符串hello拆分单个字符，两个l重复保留

items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']

# 两个数字列表拼接
print(items5 + items6)
# 输出：[35, 12, 99, 45, 66, 45, 58, 29]

# 数字列表 + 字符串列表
print(items6 + items7)
# 输出：[45, 58, 29, 'Python', 'Java', 'JavaScript']

# += 原地拼接，修改原列表items5
items5 += items6
print(items5)
# 输出：[35, 12, 99, 45, 66, 45, 58, 29]
# 解释：直接把items6全部元素追加到items5尾部


items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']

print(items6 * 3)
# 输出：[45, 58, 29, 45, 58, 29, 45, 58, 29]
# 解释：将列表完整复制3次合并为新列表

print(items7 * 2)
# 输出：['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

items7 = [45, 58, 29]
items8 = ['Python', 'Java', 'JavaScript']

print(29 in items7)  # 输出True，29在列表内
print(99 in items7)  # 输出False，99不存在
print('C++' not in items8)  # 输出True，C++不在列表
print('Python' not in items8)  # 输出False，Python存在

items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']

# ========== 正向索引读取 ==========
print(items9[0])   # 输出apple，第1个元素
print(items9[2])   # 输出pitaya，第3个元素
print(items9[4])   # 输出watermelon，最后1个元素

# ========== 正向索引修改元素 ==========
items9[2] = 'durian'
print(items9)
# 输出：['apple', 'waxberry', 'durian', 'peach', 'watermelon']
# 解释：下标2的元素被替换成榴莲

# ========== 反向索引读取 ==========
print(items9[-5])  # 输出apple，倒数第5个=第一个元素
print(items9[-4])  # 输出waxberry，倒数第4个
print(items9[-1])  # 输出watermelon，倒数第1个=最后元素

# ========== 反向索引修改元素 ==========
items9[-4] = 'strawberry'
print(items9)
# 输出：['apple', 'strawberry', 'durian', 'peach', 'watermelon']
# 解释：倒数第4位元素替换成草莓

nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]

print(nums1 == nums2)  # True，所有元素完全一致
print(nums1 != nums2)  # False，元素相同
print(nums1 <= nums3)  # True，第一个元素1 < 3
print(nums2 >= nums3)  # False，第一个元素1 < 3

languages = ['Python', 'Java', 'C++', 'Kotlin']
# len()获取列表长度，range生成0~长度-1全部下标
for index in range(len(languages)):
    print(f'下标{index}：{languages[index]}')
# 输出：
# 下标0：Python
# 下标1：Java
# 下标2：C++
# 下标3：Kotlin

languages = ['Python', 'Java', 'C++', 'Kotlin']
# 循环变量language直接接收列表每个元素
for language in languages:
    print(language)
# 输出：
# Python
# Java
# C++
# Kotlin

# 把变量名统一改为 items10
items10 = ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

# 完整格式 [start:end:stride]
print(items10[1:3:1])
# 输出：['strawberry', 'durian']
# 解释：下标1、2，步长1，不取end=3

print(items10[0:5:2])
# 输出：['apple', 'durian', 'watermelon']
# 解释：下标0、2、4，间隔2取元素

print(items10[-4:-2:1])
# 输出：['strawberry', 'durian']
# 解释：反向下标截取，-4到-2（不含-2）

print(items10[-2:-6:-1])
# 输出：['peach', 'durian', 'strawberry', 'apple']
# 解释：步长-1，从右向左反向截取

# ========== 省略参数简写写法 ==========
print(items10[1:3])      # 等价[1:3:1]，步长1省略
print(items10[:3])       # 等价[0:3:1]，start=0省略
print(items10[::2])      # 等价[0:5:2]，start、end全部省略
print(items10[-2::-1])   # 等价[-2:-6:-1]，end省略

# ========== 切片修改列表元素 ==========
items10[1:3] = ['x', 'o']
print(items10)
# 输出：['apple', 'x', 'o', 'peach', 'watermelon']
# 解释：下标1、2两个元素整体替换

# 一、列表两种遍历方式
# 方式1：通过索引遍历列表
languages = ['Python', 'Java', 'C++', 'Kotlin']
# len()获取列表长度，range生成0~长度-1全部下标
for index in range(len(languages)):
    print(f'下标{index}：{languages[index]}')
# 输出：
# 下标0：Python
# 下标1：Java
# 下标2：C++
# 下标3：Kotlin

print("-" * 30)

# 方式2：直接遍历元素（仅需要值时，推荐）
language_list = ['Python', 'Java', 'C++', 'Kotlin']
# 循环变量language直接接收列表每个元素
for language in language_list:
    print(language)
# 输出：
# Python
# Java
# C++
# Kotlin

print("=" * 40)

# 二、列表常用内置函数与方法
# 1. len(列表) 内置函数：获取列表元素总数
len_test = [10, 20, 30]
print(len(len_test)) # 输出3，列表一共有3个元素

print("-" * 30)

# 2. 列表.index(数据)：返回数据第一次出现的下标
index_test = [35, 12, 35, 87]
print(index_test.index(35)) # 输出0，35第一次出现在下标0
# 注意：数据不存在会报错ValueError

print("-" * 30)

# 3. 列表.count(数据)：统计数据在列表出现总次数
count_test = [35, 12, 35, 87, 35]
print(count_test.count(35)) # 输出3，数字35出现3次
print(count_test.count(12)) # 输出1

print("-" * 30)

# 4. 列表.append(数据)：尾部追加单个数据（原地修改）
append_test = [1, 2, 3]
append_test.append(4)
print(append_test) # 输出[1,2,3,4]
# 追加列表，整个列表作为1个元素存入
append_test.append([5,6])
print(append_test) # 输出[1,2,3,4,[5,6]]

print("-" * 30)

# 5. 列表.extend(序列)：尾部追加序列内所有元素（拆分序列）
extend_test = [1, 2, 3]
extend_test.extend([4,5])
print(extend_test) # 输出[1,2,3,4,5]
# 解释：把传入列表拆开，逐个添加，不会嵌套列表

print("-" * 30)

# 6. 列表.insert(下标, 数据)：指定下标位置插入数据
insert_test = [1, 2, 3]
# 在下标1的位置插入数字99，原下标1及之后元素后移
insert_test.insert(1, 99)
print(insert_test) # 输出[1, 99, 2, 3]

print("-" * 30)

# 7. 列表.pop(下标)：删除指定下标元素，返回被删除的值
# 不传下标默认删除最后一位
pop_test = [10, 20, 30, 40]
# 不传参数，删除最后一个元素
del_data = pop_test.pop()
print(del_data) # 输出40
print(pop_test)      # 输出[10,20,30]
# 传入下标1，删除下标1元素
del_data2 = pop_test.pop(1)
print(del_data2) # 输出20
print(pop_test)       # 输出[10,30]

print("-" * 30)

# 8. del 列表[下标/切片]：内置删除语句，无返回值
del_test = [10, 20, 30, 40]
# 删除下标1的元素
del del_test[1]
print(del_test) # [10, 30, 40]
# 切片批量删除
del del_test[1:]
print(del_test) # [10]

print("-" * 30)

# 9. 列表.remove(数据)：删除列表中第一个匹配数据
remove_test = [35, 12, 35, 87]
remove_test.remove(35)
print(remove_test) # 输出[12, 35, 87]
# 解释：只删除第一次出现的35，第二个35保留
# 注意：数据不存在会报错ValueError

print("-" * 30)

# 10. 列表.reverse()：列表原地逆序（反转），无返回值
reverse_test = [1, 2, 3, 4]
reverse_test.reverse()
print(reverse_test) # 输出[4, 3, 2, 1]

print("-" * 30)

# 11. 列表.sort()：原地升序排序，默认数字 / 字符串排序
sort_test = [99, 12, 35, 68]
sort_test.sort()
print(sort_test) # 输出[12, 35, 68, 99] 升序
# 降序排序，传入reverse=True
sort_test.sort(reverse=True)
print(sort_test) # 输出[99, 68, 35, 12]
