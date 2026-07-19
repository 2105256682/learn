# 一、整体项目需求
# 使用面向对象编程实现员工管理系统
# 持久化：员工数据存储在本地文件
# 员工数据字段：姓名 (str)、年龄 (int)、性别 (str)、手机号 (str)、是否离职 (bool)
# 全部功能列表：
# 添加员工
# 删除员工
# 修改员工信息
# 查询员工信息
# 显示所有员工信息
# 保存员工信息到文件
# 退出系统
# 二、两大核心类架构
# 类 1：Employee 员工类（单个员工实体）
# 加载、读取本地员工数据文件
# 打印系统欢迎 / 功能菜单界面
# 添加员工
# 删除员工
# 修改员工信息
# 查询员工信息
# 展示全部员工
# 将员工列表保存写入文件
# 退出系统
# 程序入口主循环函数（启动系统、循环接收用户选择）

class Employee(object):
    """员工类"""

    # is_leave=0 表示在职，1表示离职
    def __init__(self, name, gender, age, mobile_number, is_leave=0):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.is_leave = False if is_leave == 0 else True  # is_leave=true表示离职， 否则就是在职

    def __str__(self):
        msg = '离职' if self.is_leave else '在职'
        return f"{self.name}\t{self.gender}\t{self.age}\t{self.mobile_number}\t{msg}"

    # 验证模块


if __name__ == '__main__':
    e = Employee('张三', '女', '23', '123456')
    print(e.__dict__)  # 把python对象转换为字典
    print(vars(e))  # 把python对象转换为字典
    e.is_leave = True
    print(e)