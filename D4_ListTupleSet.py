course_list = ['aaa','sss','ddd','fff','ggg']
print(course_list)
print(len(course_list))
print(course_list[2])
print(course_list[-3])
print(course_list[2:4])
print(course_list[:3])

course_list.append('hhh')
print(course_list)
course_list.insert(3,'jjj')
print(course_list)

course_list2 = ['qqq','www']
course_list.insert(0,course_list2)
print(course_list)  # INSERT whole list as [['qqq', 'www'], 'aaa', 'sss', 'ddd', 'jjj', 'fff', 'ggg', 'hhh']

course_list = ['aaa','sss','ddd','fff','ggg']
course_list.extend(course_list2)  # USE extend
print(course_list)  

print('# USE remove() ')
course_list.remove('sss')  # USE remove
print(course_list)

print('USE pop() pop out from the end of list')
course_list.pop()           # USE pop from the end of list
print(course_list)

print('USE reverse() ')
course_list.reverse()       # USE reverse
print(course_list)

print('USE sort() ')
course_list.sort()       # USE sort
print(course_list)

print('USE sort() reverse ')
num = [2,4,3,1,6,5,7]
num.sort(reverse=True)
print(num)               # sort REVERSE

print('USE sorted() to a NEW LIST ')
num_sorted = sorted(num)  # sorted function
print(num_sorted)

print(min(num))
print(max(num))
print(sum(num))

print('USE index() return index of a value')
print(num)  # [7, 6, 5, 4, 3, 2, 1]
print(num.index(6))  # 6 is at index 1

print(99 in num)
print(course_list)
print('ddd' in course_list)  # USE in 


for item in course_list:
    print(item)

print('USE enumerate return index + value')
for index, course in enumerate(course_list):  # USE enumerate return index + value
    print(index, course)
print('------------------')
for index, course in enumerate(course_list,start=1):  # USE enumerate return index + value
    print(index, course)

print("# LIST to STRING: USE join() ")
course_list = ['aaa','sss','ddd','fff','ggg']
string_list = ', '.join(course_list)
print(string_list)

print("# STRING to LIST: USE split() ")
new_course_list = string_list.split(', ')
print(new_course_list)


# TUPLE : tuple can not be modified (immutable)
print('# TUPLE : tuple can not be modified (immutable)')
print('LIST')
list1 = ['History','Math','Physics','CompSci']
list2 = list1
print(list1)
print(list2)
list1[0] = 'Art'
print(list1)
print(list2)  # why list2[0] changed???

print('TUPLE')
tuple1 = ('History','Math','Physics','CompSci')
tuple2 = tuple1
print(tuple1)
print(tuple2)
#  tuple1[0] = 'Art'  # ERROR
print(tuple1)
print(tuple2)  # why list2[0] changed???



# SET : values are un-ordered and non-duplicated
print('# SET : values are un-ordered and non-duplicated')
print('SET')
set1 = {'History','Math','Physics','CompSci','Math'}
set2 = {'History','Math','Art','Design','Math'}
print(set1)
print(set2)

print('USE intersection(): ')
print(set1.intersection(set2))

print('USE difference(): ')
print(set1.difference(set2))

print('USE union(): ')
print(set1.union(set2))


print("# CREATE EMPTY LIST, TUPLE, SET: ")
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

print('empty_set = {} CREATE A EMPTY DICTIONARY')
empty_set = set()






