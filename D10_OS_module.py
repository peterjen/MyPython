import os

#print(dir(os))
print(os.getcwd())

os.chdir('C:\MyPython')
print(os.getcwd())
#print(os.listdir())

os.chdir('C:\MyPython\CoreySchafer_Tutor')
#os.mkdir('DEMO1')  
#os.makedirs('DEMO1\SUB1')
#os.removedirs('DEMO1\SUB1')
#os.rmdir('DEMO1')

#os.mkdir('DEMO2')
#os.rename('DEMO2','DEMO3')

from datetime import datetime
print(os.stat("Demo.txt"))
print(os.stat("Demo.txt").st_mtime)
print(datetime.fromtimestamp(os.stat("Demo.txt").st_mtime))

a = os.walk('C:\MyPython\CoreySchafer_Tutor')
print(a)
for dirpath, dirname, filename in a:
    print('Curr Path:',dirpath)
    print('Curr name:',dirname)
    print('Curr file:',filename)
    print()


print('----------------------')
print(os.environ)
for k,v in os.environ.items() :
    print(k,v)
print('----------------------')
print(os.environ.get('HOMEPATH'))

new_file = os.path.join(os.environ.get('HOMEPATH'),'test.txt')
print(new_file)
print(os.path.basename(new_file))
print(os.path.dirname(new_file))
print(os.path.split(new_file))
print(os.path.splitext(new_file))
print(os.path.exists(new_file))
print(os.path.isdir(new_file))
print(os.path.isfile(new_file))









