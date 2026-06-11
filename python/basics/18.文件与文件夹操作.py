import os

# 1. 查看当前目录
print("当前目录：", os.getcwd())

# 2. 列出文件
print("目录文件：", os.listdir())

# 3. 判断文件是否存在
if os.path.exists("test.txt"):
    print("test.txt 存在")
    print("文件大小：", os.path.getsize("test.txt"))

#  重命名
# os.rename("test.txt", "new.txt")

# 5. 删除文件
# os.remove("delete.txt")

