try:
    f = open('Demo.txt','r')
    a=5
    #a=5/0
    zero =1
    if zero != 0:
        raise Exception
    #for line in f:
        #pass
        #print(line,end='')
    #f.close()
#except Exception:
except FileNotFoundError as e:
    #print('file not found error')
    print(e)
except NameError as e:
    #print('Name error')
    print(e)
except Exception as e:
    print(e)
    print('ZERO != 0')
else:                       # IF no exception catch
    print('else here')
    print(f.read())
    f.close()
finally:                    # Run no matter what happened anyway
    print('Execute and Finally')










