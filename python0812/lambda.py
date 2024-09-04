# my_list =[['a',33],['b',55],['c',11]]
#
# def sort_key(element):
#     return element[1]
#
# my_list.sort(key=sort_key,reverse=True)
# print(my_list)

# my_list =[['a',33],['b',55],['c',22]]
#
# my_list.sort(key=lambda element:element[1],reverse=True)
# print(my_list)
#
# my_str='店董古居山吴'
# r1=my_str[::-1]
# print(r1)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self, other):
        return self.age<other.age

    def method(self,address):
        print(f"{address}")

# student=Student('linjie',22)
# stu2=Student('sdvfg',44)
# print(student<stu2)

class People(Student):
    def method(self,address):
        super().method(address)

p1=People('adsd',20)
print(p1.method('北京'))
