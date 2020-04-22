li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)
print('Sorted list variable\t',s_li)
print('Original list variable\t',li)

li.sort()
print('Original list \t',li)

s_li = sorted(li,reverse=True)
print('Sorted list variable\t',s_li)

print('#####################')
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Sorted tuple variable\t',s_tup)

print('#####################')
dic = {'name':'Peter','job':'SE','age':50,'DOB':None}
s_dic = sorted(dic)
print('Sorted dictionary  variable\t',s_dic)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li)
print(s_li)
s_li = sorted(li,key=abs)
print(s_li)

print('##### SORT OBJ/ CLASS ################')
class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '{} {} ${}'.format(self.name,self.age,self.salary)

e1 = Employee('Peter',50,11111)
e2 = Employee('June',40,22222)
e3 = Employee('Chloe',20,33333)

emp_li = [e1,e2,e3]
def s_emp_name(e):
    return e.name
def s_emp_age(e):
    return e.age
def s_emp_sal(e):
    return e.salary
s_emp_li = sorted(emp_li,key=s_emp_name)
print(s_emp_li)
s_emp_li = sorted(emp_li,key=s_emp_age,reverse=True)
print(s_emp_li)
s_emp_li = sorted(emp_li,key=s_emp_sal)
print(s_emp_li)

print('USE lambda function')
s_emp_li = sorted(emp_li,key=lambda e:e.name)
print(s_emp_li)
