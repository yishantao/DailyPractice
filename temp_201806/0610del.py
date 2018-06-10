import weakref

a = [1, 2, 3]
b = a


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(a, bye)
print(ender.alive)
del a
print(ender.alive)
