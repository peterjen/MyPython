import os

#print(dir(os))
print(os.getcwd())
os.chdir('C:\MyPython')
print(os.getcwd())
print(os.listdir())

os.chdir('C:\MyPython\CoreySchafer_Tutor')
os.mkdir('DEMO1')  
os.makedirs('DEMO1\SUB1')
#os.removedirs('DEMO1\SUB1')
#os.rmdir('DEMO1')

os.mkdir('DEMO2')
os.rename('DEMO2','DEMO3')



