### 字符串的索引与切片
'''...'''



### 字符串的操作


############################## capitalize()    首字母大写
'''
s = 'alexwusir'
s1 = s.capitalize()
print(s1)   # capitalize 首字母大写, Alexwusir
'''


############################## upper() 全部大写
'''
s2 = s.upper()
print(s2)   # ALEXWUSIR
'''

############################## lower() 全部小写
'''
s3 = s.lower()
print(s3)   # alexwusir
'''



############################# 随机码
'''
s_str = 'acEQ'
s_1 = s_str.lower()
print(s_1)  # aceq


you_input = input('请输入验证码，不区分大小写')
if s_str.upper() == you_input.upper():
    print('输入成功')
else:
    print('请重新重新输入')
'''


############################# swapcase() 大小写反转
'''
s3 = s.swapcase()
print(s3)
'''




############################## title()    每个隔开(特殊字符或者数字)的单词首字母大写
'''
s = 'alex*egon-wusir'
print(s.title())    # Alex*Egon-Wusir

s4 = 'fade,crazy*4rri0r_songsong node_3'
print(s4.title())   # Fade,Crazy*4Rri0R_Songsong Node_3
'''



############################## center()  剧中，空白填充
'''
s = 'alexWUsir'
s5 = s.center(20, '#')  # #####alexWUsir######
print(s5)
'''



##############################  expandtabs()  空格补白
'''
s = 'al\tsir'
s6 = s.expandtabs()
print(s6)   # al      sir
'''



##############################  公共方法
'''
s = 'fdaf sdafdasfdasfdsafdsafdsafdasfdsaUUJJJfafdaf'
l = len(s)   # 长度
print(l)    # 47

a = "按了下dafdaf"
a1 = len(a)
print(a1)   # 9
'''

## 判斷以什么开头
'''
s = 'alexWUsir'
s7 = s.startswith('alex')
# print(s7) # True
if s7:
    pass
elif s.startswith('b1'):
    pass
print(s7)
'''

############################# find()    通过元素找索引，找不到就返回-1
'''
s = 'alexWUsir'
s8 = s.find('W')
print(s8)   # 4
print(s8, type(s8))     # 4 <class 'int'>  是 int 类型
s9 = s.find('A')        # -1
print(s9)
'''



########################### index 通过元素找索引， 找不一就报错
'''
s = 'alexWUsir'
s81 = s.index('A')
print(s81)
'''


########################### strip() 默认删除前后空格，
'''
s = 'alexWUsir        '
s9 = s.strip()
print(s9)   # alexWUsir


username = input('请输入名字：').strip()
if username == '吉恩':
    print('吉恩发大财')
'''
## 删除 %
'''
s = 'alexWUsir%'
s9 = s.strip('%')
print(s9)   # alexWUsir
'''


## 删除前面的*和后面的%
'''
s = ' *alexWUsir%'
s91 = s.strip(' %*')
print(s91)  # alexWUsir

## strip() 左右都删除 rstrip()从右删除  lstrip()从左删
'''


## count    法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
'''
s = 'alex       WUslir'
s10 = s.count('l')
print(s10)  # 2
'''


## split 拆分  str -------> list 数据类型的转换
'''
# s = 'alex wusir taibai'
s = ';alex;wusir;taibai'
# l = s.split()   # ['alex', 'wusir', 'taibai']
l = s.split(';')   # ['', 'alex', 'wusir', 'taibai']
print(l)
'''


##################################### format 的三种玩，格式化输出
'''
## 第一种
s = '我叫{}, 今年{}, 爱好{}. 再说一下我叫{}'.format('吉恩', 88, 'gril', '吉恩')
print(s) # 我叫吉恩, 今年88, 爱好gril. 再说一下我叫吉恩

## 第二种
s1 = '我叫{0}, 今年{1}, 爱好{2}. 再说一下我叫{3}'.format('吉恩', 88, 'gril', '吉恩')
print(s1)   # 我叫吉恩, 今年88, 爱好gril. 再说一下我叫吉恩

## 第三种
s2 = '我叫{name}, 今年{age}, 爱好{hobby}. 再说一下我叫{name}'.format(age = 18, name='吉恩', hobby='gril')
print(s1)   # 我叫吉恩, 今年88, 爱好gril. 再说一下我叫吉恩


## 第四种
names = input('请输入名字：')
ages = input('请输入年龄：')
hobbys = input('请输入爱好：')
s3 = '我叫{name}, 今年{age}, 爱好{hobby}. 再说一下我叫{name}'
s4 = s3.format(age = ages, name=names, hobby=hobbys)
print(s4)   # 我叫cc, 今年18, 爱好打坏. 再说一下我叫cc
'''

#####################################  replace() 替换

## 替换所有的
'''
s = '我叫cc, 今年18, 爱好打坏. 再说一下我叫cc'
s11 = s.replace('cc', '吉恩') # 我叫吉恩, 今年18, 爱好打坏. 再说一下我叫吉恩
print(s11)
# 我只想替换第一个
s12 = s.replace('cc', '吉恩', 1)
print(s12)  # 我叫吉恩, 今年18, 爱好打坏. 再说一下我叫cc
'''

## ################################is 系列
'''
name1 = 'jinxing123'
name2 = 'afdafdafdafaf'
name3 = '12345'
print(name1.isalnum())   # True   方法检测字符串是否由字母和数字组成。
print(name2.isalpha())   # True  方法检测字符串是否只由字母组成。
print(name3.isdigit())   # True  方法检测字符串是否只由数字组成
'''

#################################### for 循环
'''
s = 'dafdafdafdafdafdafdsaf'
for i in s:
    print(i)

s = 'fdsa时期三坊七巷dfadas'
if '时期三坊七巷' in s:
    print('你的评论有敏感词....')
'''
