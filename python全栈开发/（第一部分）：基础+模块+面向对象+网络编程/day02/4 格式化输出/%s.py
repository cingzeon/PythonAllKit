"""
msg = "我叫吉恩，今年19 身高175"
print(msg)
"""

## 格式化输出
"""
% s d  百分号想当于占位符
s 字符串
d 是数字
"""


"""
name = input('请输入姓名')
age = input('请输入年龄')
height = input('请输入身高')
msg = "我叫%s，今年%s 身高%s" %(name, age, height)
print(msg) # 我叫吉恩，今年18 身高195
"""


"""

name = input('请输入姓名:')
age = input('请输入年龄:')
job = input('请输入工作:')
hobble = input('你的爱好:')
msg = '''
----------------- info of %s------------------
Name    ：%s
Age     : %d
Job     : %s
Hobble  : %s
---------end------------------------------------------
''' %(name, name, int(age), job, hobble)
print(msg)



''' 
输出以下结果：
----------------- info of 吉恩------------------
Name    ：吉恩
Age     : 18
Job     : 软件开发
Hobble  : 打球
---------end------------------------------------------
'''
"""


###案例
"""
name = input('请输入姓名')
age = input('请输入年龄')
height = input('请输入身高')
# msg = "我叫%s, 今年%s 身高 %s 学习进度3%%" %(name, age, height)
msg = "我叫%s, 今年%s 身高 %s 学习进度3%%s" %(name, age, height) # 我叫aln, 今年19 身高 180 学习进度3%s
print(msg)  # 我叫cc, 今年18 身高 187 学习进度3%, 前面的%号相当于转义，后面就是一个要输出的东西。
"""

count = 0
while count <= 5:
    count += 1
    if count == 3:pass
    print("Loop", count)

else:
    print("循环正常执行完啦")
print("---out of while loop --------")







