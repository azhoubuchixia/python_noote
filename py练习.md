## 数据容器

![image-20240822173107141](C:\Users\李晓慧\Desktop\笔记\image-20240822173107141.png)

```py
lst=[]
for i in range(2):
    goods=input('添加物品：')
    lst.append(goods)

for i in lst:
    print(i)

car=[]
flag=False
while True:
    shopping=input('要购买的物品：')
    for item in lst:
        if shopping==item[:4]:
            flag=True
            car.append(item)
            print('已加入购物车中')
            break

    if not flag and shopping!='q':
        print('不存在该商品')

    if shopping=='q':
        break

print('您购买的物品：')
for item in car:
    print(item)
```



![image-20240822175738367](C:\Users\李晓慧\Desktop\笔记\image-20240822175738367.png)

```py
ticket={
    'G6359':['北南-东北','18:35','19:09','00:34'],
    'G6378':['西南-西北','18:20','18:19','00:59'],
    'G6910':['东南-北东','18:15','18:49','00:34'],
}

print('车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时时长')

for key in ticket.keys():
    print(key,end='    ')
    for value in ticket[key]:
        print(value,end='\t\t')
    print()

buy_ticket=input('请输入要购买的车次：')
info=ticket.get(buy_ticket)

if info:
    people=input('请输入乘车人：')
    s=info[0]+' '+info[1]+'开'
    print(f'车次{buy_ticket} {s},请乘车人{people}换取车票。【铁路客服】')
else:
    print('车次不存在')
```



## 函数练习

<img src="C:\Users\李晓慧\Desktop\笔记\image-20240823151849163.png" alt="image-20240823151849163" style="zoom: 67%;" />

```py
def fun(x):
    s=0
    lst=[]
    for i in x:
        if i.isdigit():
            lst.append(int(i))

    s=sum(lst)
    return lst,s

s=input('请输入字符串：')
lst,x=fun(s)
print(lst)
print(x)

'''
请输入字符串：fsdhjdsklh147hkfdsh0--=1234gd
[1, 4, 7, 0, 1, 2, 3, 4]
22
'''
```



## 面向对象

<img src="C:\Users\李晓慧\Desktop\笔记\image-20240826172417409.png" alt="image-20240826172417409" style="zoom:70%;" />

```py
class Student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    def info(self):
        print(self.name,self.age,self.gender,self.score)

lst=[]
print('请输入学生信息(姓名#年龄#性别#成绩)')
for i in range(3):
    s=input(f'第{i}位学生成绩')
    s_lst=s.split('#')
    # 创建学生对象
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
    lst.append(stu)

# info方法
for i in lst:
    i.info()
```



## 第三方模块

<img src="C:\Users\李晓慧\Desktop\笔记\image-20240827092821703.png" alt="image-20240827092821703" style="zoom: 67%;" />

```py
import prettytable as pt

def show_ticket(row_num):
    tb=pt.PrettyTable() # 创建表格
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    # 遍历有票
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)

def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(1,row_num+1):
        if int(row)==i:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    row_num=6
    show_ticket(row_num)
    choose=input('收入座席(4,3):')
    row,column=choose.split(',')
    order_ticket(row_num,row,column)
```

