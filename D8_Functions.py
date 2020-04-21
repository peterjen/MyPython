def hello_func():
    print("hello")

hello_func()
#print(hello_func())

def hello_func_return():
    return 'Hello return'

print(hello_func_return().upper())

def hello_func_arg(greet, name='Ananomous'):
    return 'Hello {} >>>> {}'.format(name, greet)

print(hello_func_arg('How r u? ','Peter') )

print(hello_func_arg(name='Peter', greet='YoYo' ))
print(hello_func_arg( greet='YoYo' ))

print('# function(*args, **kwargs) : positional argument + keyword argument')
def student_info(*args, **kwargs):
    print('!!!!!!! Positional Argument in tuple:')
    print(args)
    print('!!!!!!! Keyword Argument in dictionary:')
    print(kwargs)

student_info('Math','Bio','LAL',name='John',age=15)
# ('Math', 'Bio', 'LAL')  >> tuple 
# {'name': 'John', 'age': 15}  >> dictionary

course = ['Math','Chinese','LAL']
info = {'name':'JJ','age':15}

print('This is NOT what we want:')
student_info(course,info)

print('This is what we want:')
student_info(*course,**info)
