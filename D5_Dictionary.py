student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['courses'])

print(student.get('name'))

print(student.get('phone'))
print(student.get('phone','Haha phone not found'))

student['phone'] = '555-1234'
print(student.get('phone'))

student.update({'name':'Peter','age':'50','cell':'541-0756'})
print(student)

print('# USE del to delete an item')
del student['cell']
print(student)

print('# USE pop() to delete an item')
phone = student.pop('phone')
print(student, phone)

print('# LOOP')
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, val in student.items():
    print(key, val)