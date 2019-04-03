# -*- encoding:utf-8 -*-
# print('i love cingzeon  吉恩')

"""
print(1+2+3+4) # 我想要拿到结果 * 5
print((1+2+3+4)*5)  # 50
print((1+2+3+4)*5+100-45+2) # 107

print('吉恩.......， 我是你的小弟')
print('吉恩.......， 我是你的三弟的小妹')
"""
###########变量#####################
"""
x = 1+2+3
print(x)    # 6

y = x * 5
print(y+100-45+2)   # 87
"""


####################################
"""
s = 1234
# 10r = 3 错误写法
# w*e = 4 错误写法
"""


##########以下有错误的写法##########################
'''
t-t = 2
t_t = 23
_ = 'fadsa'
__ _ =4
%- = 'adfaf'
2w = 5
qwe-r = 'wer'
'''

'''
age_of_oldboy = 56
number_of_students = 80

名字 = '成成'
print(名字) # 成成
'''
############变量##########################################
"""
age1 = 12+1   # age1 是赋值, 把右边的算完了，再赋值给前面的变量
age2 = age1
age3 = age2
age2 = 100
age3 = 5
# print(age1, age2, age3)     # 12 100 12
#   以上是从上到下，一行一行的执行的。
print(age1, age2, age3)     # 12 100 12
"""

############常量##########################################

# ADDRESS = 'CC'

###########06 基础数据类型初始##############################
"""
print(100, type(100))
print('100', type('100'))

print(1)    # 数字
print('1')  # 字符串
print("2")  # 字符串
print("I 'm a teacher") # I 'm a teacher
"""

# 字符串相加
"""
a = 'cingzeon'
b = 'CC'
c = a + b
print(c)    # cingzeonCC
print('吉恩'+'成成'+'大化') # 吉恩成成大化

print('吉恩'*8) # 吉恩吉恩吉恩吉恩吉恩吉恩吉恩吉恩

msg = '''
我们人类可以很容易的分清数字与
字符的区别，但是计算机并不能呀，
计算机虽然很强大，但从某种角度
上看又很傻，除非你明确的告诉它
'''

msga = '''
我们人类可以很容易的分清数字与
字符的区别，但是计算机并不能呀，
计算机虽然很强大，但从某种角度
上看又很傻，除非你明确的告诉它
'''

print(msg)
print(msga)
"""

## bool: 布尔值
'''
a = 4
b = 5
print(a > b)

print(True, type(True))         # True <class 'bool'>
print('True', type('True'))     # True <class 'str'>
'''

############07 用户交互input####################################
'''
name = input('请输入你的名字：')
age = input('请输入你的年龄：')
print('我的名字是：' + name + '我的年龄：' + age + '岁', type(age))    # 我的名字是：ＣＣ我的年龄：１８岁 <class 'str'>
'''

#############08 流程控制语句if#############################
'''
    if 条件
'''
### 第一种
'''
print(111)  # 666
if 5 > 4:
    print(666)  # 666
print(777)

'''

### 第二种
'''
if 4 > 5:
    print('我请你喝酒')
else:
    print('喝什么酒')



if 4 > 5:
    print('我请你喝酒')
else:
    print('喝什么酒')
'''
# 多选
'''
num = input('请输入您猜的数字：')
if num == '1':
    print('一起抽烟')
elif num == '2':
    print('一起喝酒')
elif num == '3':
    print('新开了一家， 走去看看')
else:
    print('你猜错了.....')


score = int(input('输入分数：'))
if score > 100:
    print('我擦，最高分才100....')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 60:
    print('C')
elif score >= 40:
    print('D')
else:
    print('太笨了...E')

'''


name = input('请输入名字：')
age = input('请输入年龄：')

if name == '小二':
    if age == '18':
        print(666)
    else:
        print(3333)
else:
    print('错了.....')