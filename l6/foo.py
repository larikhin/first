def foo(x):
    """ функция умножает х на 2 """
    x = x * 2
    print('foo : x * 2 = ' + str(x))
    return x
if __name__ != "__main__": 
    print('импортировали foo')
else:
    print('запустили напрямую')
