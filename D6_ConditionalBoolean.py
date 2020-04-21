lang = 'Python'

if lang == 'Python':
    print('Language is Python')
elif lang == 'Java':
    print('Language is Java')
else:
    print('Language is ' + lang)

print("# is operand: check if id()'s are equal.")
a = [1,2,3]
b = [1,2,3]

print(a==b)
print(a is b)
print('a id is ' ,id(a))
print('b id is ' ,id(b))

c=a
print('a id is ' ,id(a))
print('c id is ' ,id(c))
print(a==c)
print(a is c)

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

n = 0 #false
n = [] # false
n = ""
if n:
    print('n is true)')
else:
    print(' n is false')
