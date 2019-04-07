# int 类型
"""
i = 5
print(i.bit_length())
'''
                                bit_length
    1           0000 0001           1
    2           0000 0010           2
    3           0000 0011           3

'''
"""

# boo True False



# int ----> str 数字转换成字符串
"""
i = 1
s = str(i)  # 数字转换成字符串是没有条件的
print(s)
"""


# str ---> int
"""
s = '123'
i = int(s)
print(i)    # 123
"""

# int ---> bool  只要是0 ---> False    非0就是True
"""
i = 3
b = bool(i)
print(b)    # True

# bool ---> int
# True 1
# False 0

"""

'''
while True:
    pass

# 效率高
while 1:
    pass
'''



###################### str ---> bool 字符串布尔值
## 非空字符串都是True
"""
s = ''  # ----> False
a = '0' # ----> True
"""

"""
s = 0
if s:
    print('你输入的为空，请重新输入')
else:
    pass
"""




####################### 字符串的索引与切片
s = 'ADBCSLAFDAFDASFDAF'

# 索引值
'''
s1 = s[0]
s2 = s[1]
s3 = s[2]
print(s1, s2, s3)   # A D C
'''

#ABCD  切片，顾头不顾尾
'''
s3 = s[0:3]     #
print(s3)
'''

# 取最后一位
'''
s4 = s[-1]
print(s4)   # F
'''

# A 到 F 全部都取出来
'''
s6 = s[0:-1]
print(s6)   # ADBCSLAFDAFDASFDA
s7 = s[:]   # ADBCSLAFDAFDASFDA
'''

# ABCDLSESRF  取 ACL  s[首:尾:步长]
'''
s = 'ABCDLSESRF'
s10 = s[0:5:2]
print(s10)  # ACL
'''


# 倒着取
s = 'ABCDLSESRF'
s11 = s[4:0:-1]  # LDCB
print(s11)

s12 = s[3::-1]  # DCB
print(s12)
