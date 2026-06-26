import os

# 1. 查看当前目录
print("当前目录：", os.getcwd())

# 2. 列出文件
print("目录文件：", os.listdir())

# 3. 判断文件是否存在
if os.path.exists("test.txt"):
    print("test.txt 存在")
    print("文件大小：", os.path.getsize("test.txt"))

# 4. 重命名
# os.rename("test.txt", "new.txt")

# 5. 删除文件
# os.remove("delete.txt")

# 6目录拷贝
import os


def copy_file(source_file, sink_file):
    """
    拷贝单个文本小文件（一次性读取）
    :param source_file: 源文件绝对路径
    :param sink_file: 目标文件绝对路径
    :return: 拷贝成功之后返回1
    """
    # 第一种方案：小文件一次性读写
    with open(source_file, mode='r', encoding='utf8') as source_f:
        content = source_f.read()
    with open(sink_file, mode='w', encoding='utf8') as sink_f:
        sink_f.write(content)
    return 1

    # 第二种方案：大文件分块读写（注释备用）
    # source_f = open(source_file, mode='r', encoding='utf8')
    # sink_f = open(sink_file, mode='w', encoding='utf8')
    # while True:
    #     content = source_f.read(1024*10)  # 每次读取10KB
    #     if content == '' or content is None:
    #         break  # 文件读取完毕
    #     sink_f.write(content)
    # source_f.close()
    # sink_f.close()
    # return 1


def copy_dir(source_dir, destination_dir):
    """
    递归拷贝目录下所有.py文件，保留目录层级
    :param source_dir: 原始源目录
    :param destination_dir: 目标存放目录
    :return: 返回一共拷贝的文件数量
    """
    count = 0  # 统计拷贝文件总数
    for f in os.listdir(source_dir):
        # 拼接当前遍历项完整路径
        f_path = os.path.join(source_dir, f)

        # 情况1：是普通文件，且后缀为.py
        if os.path.isfile(f_path) and f.endswith('.py'):
            # 目标目录不存在则自动创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            # 拼接目标文件完整路径
            sink_path = os.path.join(destination_dir, f)
            # 调用单文件拷贝函数
            num = copy_file(f_path, sink_path)
            count += num

        # 情况2：是子目录，递归遍历子目录
        elif os.path.isdir(f_path):
            # 拼接递归后的新目标子目录路径，保持原目录结构
            new_destination_path = os.path.join(destination_dir, f)
            # 递归调用自身，遍历子文件夹
            sub_count = copy_dir(f_path, new_destination_path)
            count += sub_count
    return count

# 测试调用示例
# total = copy_dir(r"D:\py_workspace\django_demo6", r"D:\py_backup\py_code")
# print(f"总共拷贝了 {total} 个py文件")
# copy_file 函数
# 小文件方案：read() 一次性读取全部文本，一次性写入目标；
# 大文件方案：循环 read(1024*10) 分 10KB 块读写，避免内存溢出；
# 成功固定返回 1，用于计数累加。
# copy_dir 递归目录函数
# os.listdir() 遍历文件夹内所有文件 / 子目录名；
# os.path.join() 拼接完整绝对路径，兼容 Windows/macOS/Linux；
# os.path.isfile() 判断是否为文件 + endswith('.py') 过滤 Python 源码；
# os.makedirs() 不存在目标目录则自动创建；
# os.path.isdir() 判断子文件夹，递归调用 copy_dir，拼接新目标路径 new_destination_path 保留原目录树；
# 全局计数器累加所有拷贝成功的文件，最终返回总数。
