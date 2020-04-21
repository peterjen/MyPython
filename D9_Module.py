
print('Import D9_Module')

def find_func(search, target):
    for k,v in enumerate(target):
        #print(k,v,search)
        if v == search:
            return k
    return -1

def a_test():
    print('This is a test')