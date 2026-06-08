import random
import string


# 生成随机验证码
def generate_code(length=4):
    # 可选字符：大小写字母 + 数字
    chars = string.ascii_letters + string.digits
    # 循环随机取字符并拼接成验证码
    code = ''.join(random.choice(chars) for _ in range(length))
    return code


# 登录验证功能
def login():
    real_code = generate_code(4)
    print("验证码：", real_code)
    user_input = input("请输入验证码：")
    if user_input == real_code:
        print("登录成功")
    else:
        print("验证码错误")


login()
