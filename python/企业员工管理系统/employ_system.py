# 2. 行为（实例方法）
# 打印输出当前员工完整信息
# 类 2：EmployeeManagerSystem 员工管理系统类（业务控制器）
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

from employee import Employee
import os


class EmployeeManageSystem(object):

    def __init__(self):
        # 存放员工数据的文件
        self.employee_data_file = 'employee_data'
        # .上次保存前的员工备份文件，而且只备份一次
        self.employee_data_file_backup = 'employee.data.backup'

        self.employee_list = []  # 从文件中加载之后的员工列表

        self.save_flag = True  # 已经保存员工数据

    def main(self):
        """员工管理系统入口"""
        # 1.加载、读取本地员工数据文件
        self.load_employee()
        while True:
            # 2.显示系统欢迎界面
            self.show_hello()

            # 由用户输入指定的功能编号
            menu_number = int(input('请输入你需要的功能编号：'))

            if menu_number == 7:
                self.go_out()
                break
            elif menu_number == 1:
                self.add_employee()
            elif menu_number == 2:
                self.del_employee()
            elif menu_number == 3:
                self.update_employee()
            elif menu_number == 4:
                self.search_employee()
            elif menu_number == 5:
                self.show_all_employee()
            elif menu_number == 6:
                self.save_employee()

    def go_out(self):
        """
        推出程序的需求：如果，员工进行了添加，删除。那么必须要保存到文件中
        1.如果没有保存，则在退出之前自动保存
        :return:
        """
        if not self.save_flag:  # 员工数据没有保存
            self.save_employee()
        print('谢谢，程序结束!')

    def save_employee(self):
        """
        保存的需求和步骤：
        1.先把原来的数据文件备份（如果已经存在备份，则把备份文件删除）
        2.创建新文件5
        3.写入数据
        4.关闭文件流
        :return:
        """
        if os.path.exists(self.employee_data_file_backup):
            os.remove(self.employee_data_file_backup)  # 删除备份文件
        # 1.备份
        os.rename(self.employee_data_file, self.employee_data_file_backup)
        # 2打开文件流
        with open(self.employee_data_file, 'w', encoding="utf-8") as f:
            # 3.写入数据
            new_list = []
            for emp in self.employee_list:  # .原来的列表中是一个个的额emp对象
                # 对象不能直接保存到文件中
                new_list.append(emp.__dict__)
            # new_list  : [{'name':'zs'},{}]
            f.write(str(new_list))
        self.save_flag = True  # 刚刚已经保存过了

    def show_all_employee(self):
        """展示所有的员工信息"""
        print('姓名\t年龄\t性别\t手机号码\t是否离职')
        for emp in self.employee_list:
            print(emp)

    def search_employee(self):
        """
        根据姓名查找员工信息
        :return:
        """
        # 1.输入员工信息
        search_name = input("请输入员工姓名")
        # 2.遍历员工列表，判断是否存在
        for emp in self.employee_list:
            if emp.name == search_name:
                print(emp)
                break

    def update_employee(self):
        """
        修改员工：首先要输入修改员工姓名，然后一次修改员工的属性
        :return:
        """
        update_name = input('请输入要修改的员工姓名')
        # 2.遍历员工列表，判断是否存在，存在则修改
        for emp in self.employee_list:
            if emp.name == update_name:
                self.save_flag = False  # 你完成了一次修改，必须要保存数据
                # 3.修改员工的其他属性
                new_name = input("请输入员工姓名(不修改直接回车)：")
                emp.name = new_name if new_name else emp.name

                new_sex = input("请输入员工性别(不修改直接回车)：")
                emp.gender = new_sex if new_sex else emp.gender

                new_age = input("请输入员工年龄(不修改直接回车)：")
                emp.age = int(new_age) if new_age else emp.age

                new_number = input("请输入员工手机号码(不修改直接回车)：")
                emp.mobile_number = new_number if new_number else emp.mobile_number

                new_leave = input("请输入员工离职信息：1：离职 2：在职(不修改直接回车)：")
                if new_leave:
                    emp.is_leave = True if int(new_leave) == 1 else False

                print('员工信息已经修改完成：')
                print(emp)
                break
        else:  # 循环正常结束
            print(f'没有找到名字为{update_name}的人')

    def del_employee(self):
        """删除员工的需求，首先输入一个员工的姓名
        :return:
        """
        # 1.输入被删除的员工姓名
        del_name = input('请输入要删除的员工姓名')
        # 2.遍历员工列表，判断是否存在，存在则删除
        for emp in self.employee_list:
            if emp.name == del_name:
                self.save_flag = False  # 你完成了一次删除，必须要保存数据
                self.employee_list.remove(emp)
                print(f"名字叫{del_name}的员工已经删除")
                break
        else:
            print(f"没有找到名字为{del_name}的员工")

    def add_employee(self):
        """添加员工信息"""
        # 1.由用户输入你需要添加的员工信息
        name = input('请输入员工的姓名：')
        gender = input(str('请输入员工的性别：'))
        age = input('请输入员工的年龄：')
        mobile_number = input('请输入员工的手机号码：')
        is_leave = input('请输入员工是否离职：1表示离职，0表示在职')

        # 2，创建一个员工对象
        emp = Employee(name, gender, age, mobile_number, is_leave)
        # 3.把新加入的员工添加到列表中
        self.save_flag = False  # 你完成了一次添加，必须要保存数据
        self.employee_list.append(emp)
        # 4.把刚刚添加的员工信息，输出
        print(emp)

    @staticmethod
    def show_hello():
        """显示系统的欢迎界面"""
        print("欢迎进入企业员工管理系统")
        print('-' * 60)
        print('1:添加员工')
        print('2:删除员工')
        print('3:修改员工')
        print('4:查找员工')
        print('5:展示所有员工')
        print('6:保存员工数据')
        print('7:退出系统')
        print('-' * 60)

    def load_employee(self):
        """
        读取员工数据文件,把所有的员工信息都放到一个列表中
        :return:
        """
        try:
            f = open(self.employee_data_file, 'r', encoding="utf-8")
        except Exception as err:
            # 如果报错，很有可能第一次启动程序文件不存在，文件还需要创建一个
            f = open(self.employee_data_file, 'w', encoding="utf-8")
        else:  # 没有报错，意味着文件存在
            # 读取文件数据
            data = f.read()
            if data:
                lst = eval(data)  # 把文件的内容（字符串），当成python表达式解析
                for dict1 in lst:
                    self.employee_list.append(
                        Employee(dict1['name'], dict1['gender'], dict1['age'], dict1['mobile_number'],
                                 dict1['is_leave']))

        finally:  # 不管文件是不是报错都关闭文件
            if f:
                f.close()


if __name__ == '__main__':
    s = EmployeeManageSystem()
    s.main()
