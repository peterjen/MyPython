
f = open('Demo.txt','r')
#with open('Demo.txt','r') as f:  # will close file automatically
print(f.name)
print(f.mode)
print('-------------------')
#f_contents = f.read()  # READ IN WHOLE file
#f_contents = f.readlines() #READ IN LINES into a LIST
f_contents = f.readline() #READ IN 1 (next) line
print(f_contents)
f.close()


print('#############')
with open('Demo.txt','r') as f:  # will close file automatically
    for line in f:
        print(line,end="")
#while(f.readline() )
print('\n#############')
size_read = 10
with open('Demo.txt','r') as f:  # will close file automatically
    buffer = f.read(size_read)            # read 10 CHARs at a time
    while (len(buffer)> 0 ):
        print(buffer,end="")
        buffer = f.read(size_read)

print('\n#############')
size_read = 10
with open('Demo.txt','r') as f:  
    buffer = f.read(size_read) 
    print(buffer)
    print(f.tell())


print('\n#############')
size_read = 10
with open('Demo.txt','r') as f:  
    buffer = f.read(size_read) 
    print(buffer)
    f.seek(0)                      # Back to bigh=inning of the file (0)
    buffer = f.read(size_read) 
    print(buffer)

print('\n#############')
i = 0
with open('DemoWrite.txt','w') as f:
    for i in range(10):
        f.write('write line ' + str(i) + '\n')

with open('Demo.txt','r') as rf:
    with open('Demo_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)












