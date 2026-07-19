# 1. 序列化（dump /dumps）
# 对象 → 字节 / 字符串
# 把内存里的对象（列表、字典、自定义类实例）转换成可存储、可网络传输的文本 / 二进制数据。
# 用途：存文件、接口传数据。
# 2. 反序列化（load /loads）
# 字节 / 字符串 → 对象
# 把存好的文本 / 二进制，还原成内存里可直接操作的 Python 对象。
# 3. 两大常用模块
# json：转字符串，只能序列化基础类型（dict/list/str/int/float/bool/None），不能存自定义类对象
# pickle：转二进制字节，支持所有 Python 对象（自定义类、函数等），仅 Python 内部使用，跨语言不兼容
# 序列化（Python 对象 → JSON 文本）

#4json模块有四个比较重要的函数
# dumps()：内存转换，对象生成 JSON 字符串
# 默认中文转为 Unicode 编码，加ensure_ascii=False正常显示中文
# dump()：直接把对象序列化写入文本文件，需传入文件对象
# 反序列化（JSON 文本 → Python 对象）
# loads()：JSON 字符串还原为 Python 对象
# load()：读取文件内 JSON 数据，直接转为 Python 对象

#5
# 绝大多数网络接口返回 JSON 格式数据，用于获取天气、新闻、行业数据。
# 推荐第三方库requests，极简发送 HTTP 请求，需pip install requests安装。
# 调用流程：
# 用requests.get(接口URL)发起请求；
# 判断status_code == 200代表请求成功；
# .json()方法直接将返回 JSON 转为 Python 字典，即可读取数据。
# 接口使用前提：多数平台需注册账号获取专属 API Key 身份凭证。


import json

# 这是Python原生字典（内存里的对象）
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

# 1. dumps：Python对象 → JSON字符串（默认Unicode中文）
json_str = json.dumps(my_dict)
print("默认输出（中文转Unicode）：")
print(json_str)

# 2. 加参数，正常显示中文+格式化换行
json_str2 = json.dumps(my_dict, ensure_ascii=False, indent=2)
# indent 是 json.dumps() / json.dump() 的格式化参数，用来控制 JSON 字符串的缩进空格数，让输出的文本换行、分层，方便人阅读。
# indent=2：每一层嵌套，缩进 2 个空格。
# 不写indent：输出压缩成一整行，没有换行、无缩进，机器传输用。
print("\n优化后（可读中文、排版整齐）：")
print(json_str2)

