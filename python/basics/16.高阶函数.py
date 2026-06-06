import random
import string

# 生成随机验证码
def generate_code(length=4):
    # 可选字符：大小写字母 + 数字
    chars = string.ascii_letters + string.digits
    # 循环随机取字符并拼接成验证码
    code = ''.join(random.choice(chars) for _ in range(length))
    return code
