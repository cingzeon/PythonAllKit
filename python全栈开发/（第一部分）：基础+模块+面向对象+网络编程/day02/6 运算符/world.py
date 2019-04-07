#6 运算符



#### 逻辑运算

### and or not
"""
and 且   两边都是真，其它都是真
or  或   一边为真，其它都是真
not 非   not是真，就是假
"""
# print(2 > 1 and 1 < 4)  # True


## 优先级，() > not > and > or
# print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2 )   # True
# 第一组：2 > 1 and 1 < 4    第二组：  2 < 3 and 9 > 6  or第三组：2 < 4 and 3 < 2
# 第二组为： True  or   True  or  True
# 第三组为： True or True
# 第四组为： True
# T or T or F
# T or F



## 判断下列逻辑语句的 True, False
'''
1. 3 > 4 or 4 < 3 and 1 == 1  True 
2. 1 < 2 and 3 < 4 or 1 > 2
3. 2 > 1 and 3 < 4 or 4 > 5 and 2 < 1
4. 1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8
5. 1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
6. not 2 > 1 and 3 < 4 or 5 and 2 > 1 and 9 > 8 or 7 < 6

'''
print(3 > 4 or 4 < 4 and 1 == 1)            # True
print(1 < 2 and 3 < 4 or 1 > 2)             # True
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)   # True
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)                  # False
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)        # False
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)    # False
"""
 x or y x  为非零， 则返回x
 ps: in ---> bool 非零转换成 bool True 0 转换成 bool 是 False
 """

## bool
print(bool(2))
print(bool(-2))
print(bool(0))

## or
print(1 or 2)       # 1
print(0 or 2)       # 2
print(3 or 2)       # 3
print(0 or 100)     # 100

# bool ---> int
print(int(True))    # 1
print(int(False))   # 0


## x and y  x True, 则返回y
print(1 and 2)  # 2

print(2 or 100 or 3 or 4)   # 2
print(0 or 4 and 3 or 2)    # 3
print(3 or 2)   # 3

# 课后
print(2 or 1 < 3)                   # 2
print(2 or 1 < 3 and 2)             # 2

print(1 > 2 and 3 or 4 and 3 < 2)   # False




