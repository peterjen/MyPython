nums = [1,2,3,4,5,6,7]
for num in nums:
    print(num)

print('Break...')
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)


print('Continue...')
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

for num in nums:
    for c in 'abc':
        print(num , c)

for i in range(10): # 0 - 9
    print(i)

for i in range(1,10): # 1 (start) - 9 (end)
    print(i)

print('While loop ...')
x=0
while x < 10:
    print(x)
    x += 1

print('While loop BREAK ...')
x=0
while True:
    if x == 5:
        break
    print(x)
    x += 1
