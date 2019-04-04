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
