# ====================== 1. 四种方式创建字典（独立变量） ======================
# 方式1：{}字面量创建字典
dict_create1 = {'name': '老肖', 'age': 40}
# 空字典
dict_create2 = {}
# 方式2：dict()接收列表嵌套元组创建
dict_create3 = dict([('name', 'zs'), ('age', 44)])
# 方式3：dict()关键字参数创建
dict_create4 = dict(name='ls', age=53, city='beijing')

print("四种创建方式结果：")
print(dict_create1)
print(dict_create2)
print(dict_create3)
print(dict_create4)
print("-" * 60)

# ====================== 2. 索引操作：新增/修改键值对 dict[key] = value ======================
dict_opt1 = {'name': 'laoxiao', 'age': 34}
# 已有key：修改值
dict_opt1['age'] = 36
# 不存在key：新增键值对
dict_opt1['address'] = 'shanghai'
print("修改新增后的字典：", dict_opt1)
print("-" * 60)

# ====================== 3. del关键字删除字典键值对 ======================
dict_del_demo = {'name': '王大锤', 'age': 25, 'height': 178}
del dict_del_demo['age']
print("删除age后的字典：", dict_del_demo)
print("-" * 60)

# ====================== 4. len()、in成员运算、[]取值 ======================
dict_check = {'name': '王大锤', 'age': 55, 'height': 168}
# len() 获取键值对总数
print("字典键值对数量：", len(dict_check))
# in 判断键是否存在
print('name' in dict_check)  # True
print('tel' in dict_check)   # False
# [] 通过键取值
print("姓名：", dict_check['name'])
print("-" * 60)

# ====================== 5. get()方法安全取值（键不存在不报错） ======================
dict_get_demo = {'name': '王大锤', 'age': 25}
print(dict_get_demo.get('name'))         # 王大锤
print(dict_get_demo.get('sex'))          # None（键不存在返回空）
print(dict_get_demo.get('sex', '未知'))   # 键不存在，返回自定义默认值
print("-" * 60)

# ====================== 6. keys()、values()、items() 三大提取方法 ======================
dict_kvi = {'name': '王大锤', 'age': 25, 'height': 178}
# keys() 获取全部键
print("所有key：", dict_kvi.keys())
# values() 获取全部值
print("所有value：", dict_kvi.values())
# items() 获取全部(键,值)二元组
print("所有键值对：", dict_kvi.items())

# items() 配套for循环解包遍历（推荐）
print("\nitems遍历：")
for k, v in dict_kvi.items():
    print(f"键{k}，值{v}")
print("-" * 60)

# ====================== 7. clear() 清空字典所有数据 ======================
dict_clear_demo = {'a': 1, 'b': 2, 'c': 3}
dict_clear_demo.clear()
print("清空后的字典：", dict_clear_demo)
print("-" * 60)

# ====================== 8. fromkeys() 快速创建同默认值字典 ======================
key_list = ['name', 'age', 'tel']
dict_fromkeys = dict.fromkeys(key_list)
print("fromkeys创建字典（默认None）：", dict_fromkeys)
# 指定默认值
dict_fromkeys2 = dict.fromkeys(key_list, 0)
print("fromkeys创建字典（默认0）：", dict_fromkeys2)
print("-" * 60)

# ====================== 9. update() 合并/更新两个字典 ======================
dict_up1 = {'name': '王大锤', 'age': 55, 'height': 178}
dict_up2 = {'age': 25, 'addr': '成都武侯区'}
dict_up1.update(dict_up2)
print("update合并更新后：", dict_up1)
print("-" * 60)

# ====================== 10. pop()、popitem() 删除并返回值 ======================
dict_pop_demo = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都'}
# pop(键)：删除指定键，返回对应值
res_pop = dict_pop_demo.pop('age')
print("pop删除的age值：", res_pop)
print("pop后字典：", dict_pop_demo)

# popitem()：删除最后一组键值对，返回(键,值)元组
res_popitem = dict_pop_demo.popitem()
print("popitem删除的键值对：", res_popitem)
print("popitem后字典：", dict_pop_demo)
print("-" * 60)

# ====================== 11. 字典三种遍历方式 ======================
dict_for_demo = {'name': '小明', 'age': 18, 'city': '北京'}
# 方式1：直接遍历，只拿到key
print("只遍历键：")
for k in dict_for_demo:
    print(k, end=" ")

# 方式2：keys()遍历键
print("\n\nkeys遍历键：")
for k in dict_for_demo.keys():
    print(k, end=" ")

# 方式3：values()遍历值
print("\n\nvalues遍历值：")
for v in dict_for_demo.values():
    print(v, end=" ")

# 方式4：items()同时遍历键和值
print("\n\nitems同时遍历键值：")
for k, v in dict_for_demo.items():
    print(f"{k}={v}", end=" ")
print("\n" + "-" * 60)

# ====================== 12. zip() 双序列创建字典 ======================
dict_zip1 = dict(zip('ABCDE', '12345'))
dict_zip2 = dict(zip('ABCDE', range(1, 10)))
print("zip字符串配对：", dict_zip1)
print("zip字符+数字：", dict_zip2)
print("-" * 60)

# ====================== 13. 字典生成式（筛选、快速造字典） ======================
# 基础生成式
dict_gen1 = {x: x ** 3 for x in range(1, 6)}
print("基础字典生成式：", dict_gen1)

# 带条件筛选的生成式（股价大于100）
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44
}
stocks_filter = {k: v for k, v in stocks.items() if v > 100}
print("筛选股价>100的股票：", stocks_filter)
print("-" * 60)

# ====================== 14. 实战案例：统计字母出现次数 ======================
sentence = "Man is distinguished, not only by his reason"
counter_dict = {}
for ch in sentence:
    # 判断是否英文字母
    if ch.isalpha():
        # get快速计数，不存在则默认0
        counter_dict[ch] = counter_dict.get(ch, 0) + 1
# 按次数降序排序
sorted_chars = sorted(counter_dict, key=counter_dict.get, reverse=True)
print("字母统计结果（降序）：")
for char in sorted_chars:
    print(f"{char} 出现 {counter_dict[char]} 次")