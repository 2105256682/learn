my_name = '张三'
my_age = 18
my_city = 'hubei'

print('我的名字是张三')

print('我的名字是%s' % my_name)
print('我的名字是%s, 我的年龄是%d, 我所在的城市%s' % (my_name, my_age, my_city))

# 特殊的格式
money = 8923
num = 1.71

print('我的金额是：%5d' % money)
print('我的金额是：%d' % money)

#精确到小数点后一位: 四舍五入，不做处理是不准确的
print('%.1f' % num)

num02 = 22.345
print('%.2f' % num02)

#精确的四舍五入
from decimal import Decimal
Decimal('22.345')
print(Decimal(str(num02)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))