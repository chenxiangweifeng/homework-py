# -*- coding: utf-8 -*-
import time
import calendar
'''
utf-8格式编码的语句一定要放在第一行
utf-8格式编码的语句一定要放在第一行
python数据类型：
numbers
string
list
tuple
dictionary
python没有boolean类型
'''
print("大幅度发但是但是多")
str = "hello world"
print str[2:5]
list = ['aaa', '23', 30.4, 'bbb']
print list[0]
#  元组是只读列表 不能修改里面的值，list就是一个数组
tuple = ('runboot', 88, 'fdfd',90.3)
# python中的字典是除了列表之外的应用最为灵活的数据结构类型，字典当中的元素是通过key来存取的，类似map集合
# 用来存取一个对象是非常的方便
tinydict = {'name': 'alice', 'age': 18, 'address': 'beijing'}

for l in list:
    print l
# 字典的遍历
for key in tinydict:
    print ("key===", key)
    print ("value===", tinydict[key])

print list
del list[2]
print ('old',list)

var = 1
while var < 20:
    var += 1
    if var == 8:
        break
    print var

name = "alice"
length = len(name)
print ("长度是：")
print length

print time.localtime(time.time())

def myfun(a , b):
    out1 = a - b
    out2 = a + b
    return [out1, out2]

[result1, result2] = myfun(18, 5)
print result1, result2





















