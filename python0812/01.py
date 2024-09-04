# print('你好',end='-->')
# print('北京',end='...')
# print('nihao','beij')
# fp=open('note.txt','w')
# print('北京欢迎你',file=fp)
# fp.close()
#
# import keyword
# print(len(keyword.kwlist))

# s='3.14+3'
# print(s)
# x=eval(s)
# print(x)
#
# a,b=10 ,'sdfkjk'
# print(a,b)
#
# a,b=b,a
# print(a,b)

# y=input('输入：')
# if not y:
#     print('s')
# else:
#     print(y)

# a=eval(input('输入：'))
#
# a1=a//1000
# a2=a//100%10
# a3=a%100//10
# a4=a%100%10
# print("个位上的数：",a4)
# print("十位上的数：",a3)
# print("百位上的数：",a2)
# print("千位上的数：",a1)

# for i in range(1,5):
#     print(i)
# else:
#     print('22222')

# str=list('sass')
# print(str)
# str1=list(range(1,5))
# print(str1)

# 可迭代对象示例
# my_list = ['a','b','c']
# for item in my_list:  # my_list是可迭代对象
#     print(item)
#
# print('----------------------')
# # 迭代器示例
# my_iter = iter(my_list)  # 通过iter()获取迭代器
# while True:
#     try:
#         item = next(my_iter)  # 使用迭代器的__next__()方法
#         print(item)
#     except StopIteration:
#         print('迭代结束')
#         break  # 迭代器耗尽时，抛出StopIteration异常


# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# for key, value in my_dict.items():
#     print(f'Key: {key}, Value: {value}')
# print('--------------')
#
#
# # 获取字典items()方法的迭代器
# items_iter = iter(my_dict.items())
#
# # 使用next()函数来手动迭代
# try:
#     while True:  # 使用无限循环来模拟迭代过程
#         key, value = next(items_iter)  # 显式调用next()获取下一项
#         print(f'Key: {key}, Value: {value}')
# except StopIteration:
#     # 当迭代器耗尽时，捕获StopIteration异常
#     print('迭代结束')



# for index,item in enumerate(my_list):
#     print(index,item)         # index是序号，不是索引
#
# print('------------------')
# # 手动修改序号的起始值,start可以省略不写
# for index,item in enumerate(my_list,start=1):
#     print(index,item)

# import random
# list=[item for item in range(10)]
# print('list:',list)
#
# list2=[item*item for item in range(1,11)]
# print('list2:',list2)
#
# list3=[random.randint(1,100) for _ in range(10)]
# print('list3',list3)
#
# list4=[i for i in range(10) if i%2==0]
# print('list4:',list4)
#
# s=[
#     ['类型','分值','等级'],
#     ['A',90,'优秀'],
#     ['C',60,'及格'],
#     ['B',80,'良好'],
# ]
# print(s)
#
# # 遍历二维列表，双层for循环
# for row in s:
#     for item in row:
#         print(item,end='\t')
#     print()
#
# # 生成二维列表
# lst=[[j for j in range(5)] for i in range(4)]
# print(lst)

# 定义一个元组
# t=('python','java','golang')
# print(t[0]) # 索引访问
#
# # 切片
# t2=t[0:3:2]
# print(t2)
#
# # 遍历
# for item in t:
#     print(item)
#
# # for+range+len()
# for item in range(len(t)):
#     print(item,t[item])
#
# # enumerate()
# for index,item in enumerate(t,1):
#     print(index,'--->',item)

# d={10:'cat',40:'bag',30:'fag'}
# print(d)
#
# lst1=[10,20,30]
# lst2=['car','gff','fdwe']
# z=zip(lst1,lst2)
# # print(z) # <zip object at 0x000001D19873B780>
# # print(list(z)) #[(10, 'car'), (20, 'gff'), (30, 'fdwe')]
# y=dict(z)
# print(y)  # {10: 'car', 20: 'gff', 30: 'fdwe'}

# d={'mike':10,'jack':18,'rose':21}
# print(d.get('jack'))  # 18
#
# # 遍历
# for item in d.items():
#     print(item)
# '''
# ('mike', 10)
# ('jack', 18)
# ('rose', 21)
# '''
#
# for key,value in d.items():
#     print(key,'----->',value)
# '''
# mike -----> 10
# jack -----> 18
# rose -----> 21
# '''

# import random
# d={item:random.randint(1,10) for item in range(4)}
# print(d)  # {0: 2, 1: 1, 2: 3, 3: 10}
#
# lst1=[10,20,30]
# lst2=['car','gff','fdwe']
# a={key:value for key,value in zip(lst1,lst2)}
# print(a)  # {10: 'car', 20: 'gff', 30: 'fdwe'}

# s={10,20,30}
#
# for item in s:
#     print(item)
# '''
# 10
# 20
# 30
# '''
#
# for index,item in enumerate(s):
#     print(index,'---->',item)
# '''
# 0 ----> 10
# 1 ----> 20
# 2 ----> 30
# '''
# s={i for i in range(10)}
# print(s) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# s={i for i in range(1,10) if i%2==1}
# print(s)  # {1, 3, 5, 7, 9}

# data=eval(input('请输入：'))
# match data:
#     case {'name':'ls','age':20}:
#         print('字典')
#     case [10,20,30]:
#         print('列表')
#     case (10,20,30):
#         print('元组')
#     case _:
#         print('相当于多重if中的else')

# d1={'a':'ls','b':20}
# d2={'c':'ls','d':20}
# m=d1|d2
# print(m)  # {'a':'ls','b':20,'c':'ls','d':20}

# lst=[]
# for i in range(2):
#     goods=input('添加物品：')
#     lst.append(goods)
#
# for i in lst:
#     print(i)
#
# car=[]
# flag=False
# while True:
#     shopping=input('要购买的物品：')
#     for item in lst:
#         if shopping==item[:4]:
#             flag=True
#             car.append(item)
#             print('已加入购物车中')
#             break
#
#     if not flag and shopping!='q':
#         print('不存在该商品')
#
#     if shopping=='q':
#         break
#
# print('您购买的物品：')
# for item in car:
#     print(item)

# ticket={
#     'G6359':['北南-东北','18:35','19:09','00:34'],
#     'G6378':['西南-西北','18:20','18:19','00:59'],
#     'G6910':['东南-北东','18:15','18:49','00:34'],
# }
#
# print('车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时时长')
#
# for key in ticket.keys():
#     print(key,end='    ')
#     for value in ticket[key]:
#         print(value,end='\t\t')
#     print()
#
# buy_ticket=input('请输入要购买的车次：')
# info=ticket.get(buy_ticket)
#
# if info:
#     people=input('请输入乘车人：')
#     s=info[0]+' '+info[1]+'开'
#     print(f'车次{buy_ticket} {s},请乘车人{people}换取车票。【铁路客服】')
# else:
#     print('车次不存在')

# str='伟大的中国梦'
#
# # 编码
# str_code=str.encode()
# print(str_code)
# # 解码
# str_decode=bytes.decode(str_code)
# print(str_decode)

# import re
# pattern='\d\.\d+' #0-9数字出现1次或多次
# s='i am study py 3.11 day by day'
# match=re.match(pattern,s,re.I)
# print(match) # None
#
# s2='3.11 py day'
# match2=re.match(pattern,s2)
# print(match2)  # <re.Match object; span=(0, 4), match='3.11'>
#
# match3=re.search(pattern,s)
# print(match3)  # <re.Match object; span=(14, 18), match='3.11'>
#
# match4=re.findall(pattern,s)
# print(match4)  # ['3.11']
#
# pattern2='黑客|破解'
# s3='爬虫腾讯，破解VIP视频，用黑客身份实现'
# match5=re.sub(pattern2,'***',s3)
# print(match5)  # 爬虫腾讯，***VIP视频，用***身份实现
#
# pattern3='[?|%]'
# s4='https://baike.sogou.com/v4297323.htm?fromTitle=%E8%B5%B5%E4%B8%BD%E9%A2%96'
# match6=re.split(pattern3,s4)
# print(match6)  # ['https://baike.sogou.com/v4297323.htm', 'fromTitle=', 'E8', 'B5', 'B5', 'E4', 'B8', 'BD', 'E9', 'A2', '96']

# s = '中国梦'
# lst = ['伟大', '魅力']
# s2 = s.join(lst)
# print(s2)

# try:
#     gender=input('输入性别：')
#     if gender!='男' and gender!='女':
#         raise  Exception('性别只能是男或女')
#     else:
#         print(f'您的性别是{gender}')
# except Exception as e:
#     print(e)

# def ninao(name,age):
#     print(f'{name}您好,{age}岁生日快乐')
#
# ninao('jack',18)

# # 普通函数
# def calc(a,b):
#     return a+b
#
# print(calc(10,20))  # 30
#
# # 匿名函数
# s=lambda a,b:a+b
# print(type(s)) # <class 'function'>
# print(s(10,20)) # 30

# lst=[10,20,30,40,50]
#
# for i in range(len(lst)):
#     print(i)
#     result = lambda x:x[i]
#     print(result)
#     print(result(lst))

# my_list=[
#     ['a',30],
#     ['b',20],
#     ['c',50]
# ]
# my_list.sort(key=lambda x:x[1],reverse=True)
# print(my_list)  # [['c', 50], ['a', 30], ['b', 20]]

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
#
# print(fac(5))


# def fac(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fac(n-1)+fac(n-2)
#
# print(fac(9)) #34
#
# for i in range(1,10):
#     print(fac(i),end='\t')
# print()  #  1	1	2	3	5	8	13	21	34

# print('非空字符串:',bool('hello')) # 非空字符串: True
# print('空字符串:',bool(''))       # 空字符串: False
#
# lst=[10,20,30]
# print(type(lst))                # <class 'list'>
# print(type(str(lst)))           # <class 'str'>
#
# print(int(98.7)+int('10'))      # 108
#
# print(float(90)+float(3.14))    # 93.14
#
# str='word'
# print(list(str))                # ['w', 'o', 'r', 'd']
# print(tuple(str))               # ('w', 'o', 'r', 'd')
# print(set(str))                 # {'d', 'r', 'o', 'w'}

# def fun(num):
#     return num%2==1
#
# obj=filter(fun,range(10))  # 将range(10),0-9的整数都执行一次fun操作,只有True才会给obj
# print(obj)  # <filter object at 0x00000225134EF700>
# print(list(obj))  # [1, 3, 5, 7, 9]
#
# def upper(x):
#     return x.upper()
#
# lst=['hello','world','python']
# obj2=map(upper,lst)
# print(obj2)  # <map object at 0x000001677BB047C0>
# print(list(lst))  # ['hello', 'world', 'python']

# def fun(x):
#     s=0
#     lst=[]
#     for i in x:
#         if i.isdigit():
#             lst.append(int(i))
#
#     s=sum(lst)
#     return lst,s
#
# s=input('请输入字符串：')
# lst,x=fun(s)
# print(lst)
# print(x)

# class Parent:
#     def __init__(self,name):
#         self.name=name
#
# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#
# s=Child('jack',18)
# print(s.name)

# class FatherA:
#     def __init__(self,name):
#         self.name=name
#
#     def showA(self):
#         print('父类A的方法')
#
#
# class FatherB:
#     def __init__(self, name):
#         self.name = name
#
#     def showB(self):
#         print('父类B的方法')
#
# class Son(FatherA,FatherB):
#     def __init__(self,name,age,gender):
#         FatherA.__init__(self,name)
#         FatherB.__init__(self,age)
#         self.gender=gender
#
# son=Son('jack',18,'男')
# son.showA()
# son.showB()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show(self):
#         print(f'大家好，我是{self.name},今年{self.age}岁')
#
# class Student(Person):
#     def __init__(self, name, age,stuno):
#         super().__init__(name,age)
#         self.stuno=stuno
#
#     def show(self):
#         # 调用父类中的方法（也可以不调用）
#         super().show()
#         print(f'我来自xxx大学，学号是{self.stuno}')
#
# class Doctor(Person):
#     def __init__(self, name, age,deparment):
#         super().__init__(name,age)
#         self.deparment=deparment
#
#     def show(self):
#         print(f'大较好，我叫{self.name},工作科室{self.deparment}')
#
# stu=Student('陈美美',18,'1234')
# stu.show()  # 调用子类自己的show()方法
#
# doctor=Doctor('jack',24,'心外科')
# doctor.show()  # 调用子类自己的show()方法

# a=10
# b=20
# print(dir(a))  # python中一切皆对象
# print(a.__add__(b))   # 30
# print(a.__sub__(b))   # -10
# print(a.__lt__(b))    # True
# print(a.__le__(b))    # True
# print(a.__eq__(b))    # False

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
# stu1=Student('jack',13)
# stu2=Student('cc',24)
# print(stu1<=stu2)  # True
# print(stu1>=stu2)  # False

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# a=A()
# b=B()
# c=C('jakc',25)
#
# print(a.__dict__)  # {}
# print(b.__dict__)  # {}
# print(c.__dict__)  # {'name': 'jakc', 'age': 25}
#
# print(a.__class__) # <class '__main__.A'>
# print(b.__class__) # <class '__main__.B'>
# print(c.__class__) # <class '__main__.C'>
#
# print(A.__base__) # <class 'object'>
# print(B.__base__) # <class 'object'>
# print(C.__base__) # <class '__main__.A'>  如果继承了多个父类，结果只显示第一个父类
#
# print(A.__bases__) # (<class 'object'>,)
# print(B.__bases__) # (<class 'object'>,)
# print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)
#
# print(A.__mro__) # (<class '__main__.A'>, <class 'object'>)
# print(B.__mro__) # (<class '__main__.B'>, <class 'object'>)
# print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>) C类首先继承了A,B类，间接继承了object类

# import copy
# class CPU:
#     pass
# class Disk:
#     pass
# class Computer:
#     def __init__(self,cpu,disk):
#         self.cpu=cpu
#         self.disk=disk
#
# cpu=CPU()
# disk=Disk()
#
# com=Computer(cpu,disk)
# print(com)
#
# com1=com
# print(com1,com1.cpu,com1.disk)
#
# print('-'*40)
# # 浅拷贝
# com2=copy.copy(com1)
# print(com2,'浅拷贝的子对象内存地址：',com2.cpu,com2.disk)
#
# print('-'*40)
# # 深拷贝
# com3=copy.deepcopy(com1)
# print(com3,'深拷贝的子对象内存地址',com3.cpu,com3.disk)

# class Student:
#     def __init__(self,name,age,gender,score):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.score=score
#
#     def info(self):
#         print(self.name,self.age,self.gender,self.score)
#
# lst=[]
# print('请输入学生信息(姓名#年龄#性别#成绩)')
# for i in range(3):
#     s=input(f'第{i}位学生成绩')
#     s_lst=s.split('#')
#     # 创建学生对象
#     stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
#     lst.append(stu)
#
# # info方法
# for i in lst:
#     i.info()

# import requests
# import re
# import openpyxl
#
# def get_html():
#     url = 'https://www.weather.com.cn/weather1d/101010100.shtml#search'
#     resp = requests.get(url)
#     resp.encoding = 'utf-8'
#     return resp.text
#
# def parse_html(html_str):
#     city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', html_str)
#     weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', html_str)
#     wd = re.findall('<span class="wd">(.*)</span>', html_str)
#     zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', html_str)
#
#     lst = []
#     for a, b, c, d in zip(city, weather, wd, zs):
#         lst.append([a, b, c, d])
#     # print(lst)
#     return lst
#
# data=parse_html(get_html())
# print(data)
# # 创建Excel
# workbook=openpyxl.Workbook()
# # 在Excel中创建表
# sheet=workbook.create_sheet('景点天气')
# # 添加数据
# for i in data:
#     sheet.append(i)
#
# workbook.save('景区天气.xlsx')

# import openpyxl
# # 打开工作簿
# workbook=openpyxl.load_workbook('景区天气.xlsx')
# # 选择要操作的工作表
# sheet=workbook['景点天气']
# lst=[]
# # 表格数据是二维数列，先遍历行，再遍历列
# for row in sheet.rows:
#     sub_lst=[]  # 存储单元格数据
#     for cell in row:  # 单元格
#         sub_lst.append(cell.value)
#     lst.append(sub_lst)
#
# for i in lst:
#     print(i)

# import numpy
# import matplotlib.pyplot as plt
#
# # 读取图像
# n1 = plt.imread('img.png')
#
# # 确保图像是RGB格式的
# if n1.ndim == 3 and n1.shape[2] == 4:  # 如果图像是RGBA
#     n1 = n1[..., :3]  # 只保留RGB通道
#
# # 转换为灰度图像
# n2 = numpy.array([0.299, 0.587, 0.114])
# gray_image = n1.dot(n2)  # 沿着最后一个维度进行点积
#
# # 显示灰度图像
# plt.imshow(gray_image, cmap='gray')
# plt.show()

# import prettytable as pt
#
# def show_ticket(row_num):
#     tb=pt.PrettyTable() # 创建表格
#     tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
#     # 遍历有票
#     for i in range(1,row_num+1):
#         lst=[f'第{i}行','有票','有票','有票','有票','有票']
#         tb.add_row(lst)
#     print(tb)
#
# def order_ticket(row_num,row,column):
#     tb=pt.PrettyTable()
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(1,row_num+1):
#         if int(row)==i:
#             lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
#             lst[int(column)]='已售'
#             tb.add_row(lst)
#         else:
#             lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
#             tb.add_row(lst)
#     print(tb)
#
# if __name__ == '__main__':
#     row_num=6
#     show_ticket(row_num)
#     choose=input('收入座席(4,3):')
#     row,column=choose.split(',')
#     order_ticket(row_num,row,column)

# def my_write(file,lst):
#     f=open(file,'a',encoding='utf-8')
#     f.writelines(lst)
#     f.close()
#
# lst=['姓名\t','年龄\t','成绩\n','张三\t','18\t','90\t']
# my_write('1.txt',lst)

# with open('1.txt','a',encoding='utf-8') as f:
#     f.write('你好世界')
#
# with open('1.txt','r',encoding='utf-8') as f:
#     print(f.read())
#
# with open('1.txt','r',encoding='utf-8') as f:
#     with open('2.txt','w',encoding='utf-8') as f2:
#         f2.write(f.read())

# import json
# lst=[
#     {'name':'jack','age':18,'score':90},
#     {'name':'lisi','age':24,'score':79},
#     {'name':'zs','age':20,'score':88}
# ]
# # json格式
# lst_json=json.dumps(lst,ensure_ascii=False,indent=4)  # ensure_ascii正常显示中文，index增加数据的缩进
# print(lst_json)
#
# # 解码json格式
# lst2=json.loads(lst_json)
# print(lst2)  # [{'name': 'jack', 'age': 18, 'score': 90}, {'name': 'lisi', 'age': 24, 'score': 79}, {'name': 'zs', 'age': 20, 'score': 88}]
#
# # 编码到文件中
# with open('student.txt','w') as file:
#     json.dump(lst,file,ensure_ascii=False,indent=4)  # 转存到文件中

# def outer(logo):
#
#     def inner(msg):
#         print(f'{logo}---{msg}---{logo}')
#
#     return inner
#
# s=outer('nihao')
# s('世界')  # nihao---世界---nihao


# def create_closure():
#     # 外部函数的变量
#     external_var='i am external'
#
#     def closure():
#         return external_var
#
#     return closure
#
# # 创建闭包
# my_closure=create_closure()
# # 调用闭包
# print(my_closure())   # i am external

# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1  # 需要使用nonlocal关键字修饰外部函数的变量才可在内部函数中修改它
#         # num1=5
#         num1 += num2
#         print(num1)
#
#     return inner
#
# s=outer(10)
# s(10)  # 20

# def account_create(initial_amount):
#
#     def atm(num,deposit=True):
#         nonlocal initial_amount
#         if deposit:
#             initial_amount += num
#             print(f'存款：+{num},账户余额：{initial_amount}')
#         else:
#             initial_amount -=num
#             print(f'取款：-{num},账户余额：{initial_amount}')
#     return atm
#
# initial_amount=0
# atm=account_create(initial_amount)
# atm(100)                    # 存款：+100,账户余额：100
# atm(10,False)  # 取款：-10,账户余额：90
# '''
# initial_amount 作为 account_create 函数的局部变量，在 account_create 返回后并没有被销毁，因为 atm 闭包持有对其的引用。
# 所以，initial_amount 的值在两次调用之间是持续存在的，并且保持了其状态。
# 闭包 atm 记住了 initial_amount 的值，即使 account_create 函数已经执行完毕。每次调用 atm 时，都是基于 initial_amount 当前的值来进行操作的。
# '''

# outer()函数是一个装饰器
# def outer(func):
#     # 闭包函数inner()
#     def inner():  # 这个函数应该接收调用func时传入的参数
#         print('睡觉....')
#         func()  # 调用原始的sleep函数
#         print('起床了')
#     return inner
#
# @outer  # 这相当于 sleep = outer(sleep)，将装饰器outer应用于sleep函数
# def sleep():
#     print('睡眠中')
#
# sleep()  # 调用被装饰后的sleep函数，实际上是在调用被 outer 装饰的 inner 函数。

# 服务端
import socket

# 1.创建socket对象
server_socket=socket.socket()

# 2.绑定IP地址和端口
ip='127.0.0.1'
port=8888
server_socket.bind((ip,port))

# 3.使用listen()监听
server_socket.listen(5)
print('服务已启动')

# 4.等待客户端连接
client_socket,client_addr=server_socket.accept()  # 解包赋值

# 5.接收客户端传来的数据
data=client_socket.recv(1024)
print('客户端传来的数据：',data.decode('utf-8'))

# 6.关闭socket
server_socket.close()